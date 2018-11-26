import configparser
from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField
from wtforms.validators import DataRequired
from datetime import datetime


# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)
# TODO: put this in the config.ini
app.config['SECRET_KEY'] = 'ssssh!'


class NewEmployeeForm(FlaskForm):
    """
	Class to handle the new employee field
    """
    name = StringField('Name',validators=[DataRequired()])
    start_date = DateField('Start Date',validators=[DataRequired()])
    end_date = DateField('End Date')


# Create a function for fetching data from the database.
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

@app.route('/emp/<emp_id>',methods=['GET','POST'])
def employee_view(emp_id):
    if "delete-device" in request.form:
        device_id = int(request.form["delete-device"])
        sql = "delete from Device where device_id={device_id};".format(device_id=device_id)
        sql_execute(sql)

    # Get info about this specific employee or return a 404
    sql = "select * from Employee where employ_id="+str(emp_id)+";"
    employee = sql_query(sql)
    if not employee:
        return "ERROR 404: Employee ID Not found in database."
    template_data = {}
    template_data['emp_data'] = employee
    # Get information about devices that have not been issued to any employee
    sql = str(open('unissued_devices.sql','r').read())
    devices = sql_query(sql)
    template_data['u_devices'] = devices
    if 'issue-device' in request.form:
        device_id = int(request.form['issue-device'])
        sql = "INSERT INTO issued_to VALUE("
        sql += "'"+str(emp_id)+"',"
        sql += "'"+str(device_id)+"',"
	# make the date of issuing today
        today = datetime.today()
        sql += "'"+str(today.year)+"-"+str(today.month)+"-"+str(today.day)+"',"
        sql += "NULL);"
        sql_execute(sql)
    # Get information about the devices issued to this employee
    sql = "select d.* from Device d , issued_to it where d.device_id=it.device_id and it.employ_id="+str(emp_id)+";"
    devices = sql_query(sql)
    template_data['devices'] = devices

    return render_template('employee.html',template_data=template_data) 
	


@app.route('/', methods=['GET', 'POST'])
def company_view():
    form = NewEmployeeForm()
    if  'add-employee' in request.form and form.validate():
        # Get biggest emp id ... this should be handled on the db levl
        sql = 'INSERT INTO Employee (name,start_date,end_date) Values('
        sql += "'"+str(form.name.data)+"',"
        sql += "'"+str(form.start_date.data)+"',"
        try:
	        sql += "'"+str(form.end_date.data)+"'"
        except:
            sql += "NULL"
        sql += ");"
        sql_execute(sql)
    if 'delete-employee' in request.form:
        emp_id = int(request.form['delete-employee'])
        sql = "DELETE FROM Employee WHERE employ_id="+str(emp_id)+";"
        sql_execute(sql)

    print(request.form)
    template_data = {}
    sql = "SELECT Employee.employ_id, name, start_date,end_date, count(device_id)\
		FROM\
		Employee \
		left join issued_to  on Employee.employ_id=issued_to.employ_id\
		group by\
		Employee.employ_id;\
	"
    employees = sql_query(sql)
    template_data['employees'] = employees 


    # Get company wide stats
    sql = "select count(1) from Employee;"
    num_emp = int(sql_query(sql)[0][0])
    num_devices = int(sql_query("select count(1) from Device")[0][0])
    outstanding_devices = int(sql_query("select count(1) from issued_to where returned_date is NULL")[0][0])
    template_data['stats'] = [num_emp,num_devices,outstanding_devices]
    
    print(template_data)
    return render_template('company.html', template_data=template_data, form=form) 

if __name__ == '__main__':
    app.run(**config['app'])

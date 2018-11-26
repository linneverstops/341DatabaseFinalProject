import configparser
from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField
from wtforms.validators import DataRequired



# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ssssh!'


# Form for new device
class NewDeviceForm(FlaskForm):
    dtype = StringField('Device Type',validators=[DataRequired()])
    make = StringField('Make',validators=[DataRequired()])
    model = StringField('Model',validators=[DataRequired()])
    serial_num = IntegerField('Serial Number',validators=[DataRequired()])
    # TODO: additional date validation?
    exp_date = DateField('Warenty Expiration Date',validators=[DataRequired()])    



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

def build_add_device_query(form):
    pass


@app.route('/emp/<emp_id>',methods=['GET','POST'])
def employee_view(emp_id):
    form = NewDeviceForm()
    if "delete-device" in request.form:
        device_id = int(request.form["delete-device"])
        sql = "delete from Device where device_id={device_id};".format(device_id=device_id)
        sql_execute(sql)
    if 'add-device' in request.form:
	# Parse SQL here
	sql = build_add_device_query(request.form)

        if form.validate_on_submit():
            return redirect('/emp/'+str(emp_id))


    # Get info about this specific employee or return a 404
    sql = "select * from Employee where employ_id="+str(emp_id)+";"
    employee = sql_query(sql)
    if not employee:
        return "ERROR 404: Employee ID Not found in database."
    template_data = {}
    template_data['emp_data'] = employee
    # Get information about the devices issued to this employee
    sql = "select d.* from Device d , issued_to it where d.device_id=it.device_id and it.employ_id="+str(emp_id)+";"
    devices = sql_query(sql)
    template_data['devices'] = devices	


    return render_template('employee.html',template_data=template_data, form=form) 
	


@app.route('/', methods=['GET', 'POST'])
def company_view():
    print(request.form)
    #if "buy-book" in request.form:
    #    book_id = int(request.form["buy-book"])
    #    sql = "delete from book where id={book_id}".format(book_id=book_id)
    #    sql_execute(sql)
    template_data = {}
    sql = "select e.employ_id, e.name, e.start_date,e.end_date, count(it.device_id) from Employee e, issued_to it where e.employ_id=it.employ_id group by e.employ_id;"
    employees = sql_query(sql)
    template_data['employees'] = employees 
    print(template_data)
    return render_template('company.html', template_data=template_data) 

if __name__ == '__main__':
    app.run(**config['app'])

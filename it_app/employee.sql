SELECT name, start_date,end_date, count(device_id)
FROM
Employee 
left join issued_to  on Employee.employ_id=issued_to.employ_id
group by
Employee.employ_id;

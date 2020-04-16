import cx_Oracle
import os
import flask
from flask import Flask, jsonify, request


connection = cx_Oracle.connect(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_CONNECTIONSTRING'])

cursor = connection.cursor()
rs = cursor.execute("select 'Hello for ADB' from dual")
print(rs.fetchall())
rs = cursor.execute("select current_timestamp from dual")
print(rs.fetchall())
rs = cursor.execute("SELECT * FROM HR.EMPLOYEES")
print(rs.fetchall())
print('hola')


# Conteo de registros de todas las tablas de HR
@app.route('/count')
def count():
   rs = cursor.execute("select sum(to_number(extractvalue(xmltype(dbms_xmlgen.getxml('select count(*) c from '||table_name)),'/ROWSET/ROW/C'))) count from user_tables")
   print(rs.fetchall())

app = Flask(__name__)
#app.config["DEBUG"] = True

# things
@app.route('/employees', methods=['GET'])
def employees():
    data = request.get_json()
    opt = data.get('opt')
    e_id = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    hire_date = data.get('hire_date')
    job_id = data.get('job_id')
    salary = data.get('salary')
    comission_pct = data.get('comission_pct')
    manager_id = data.get('manager_id')
    department_id = data.get('department_id')
    

    if opt is 'insert':
        sql = f"""insert into employees 
            (
                employee_id, 
                first_name, 
                last_name, 
                email, 
                phone_number, 
                hire_date, 
                job_id, 
                salary, 
                comission_pct, 
                manager_id, 
                department_id
            )
        values 
            (
                :employee_id, 
                :first_name, 
                :last_name, 
                :email, 
                :phone_number, 
                :hire_date, 
                :job_id, 
                :salary, 
                :comission_pct, 
                :manager_id, 
                :department_id
            )"""
        values = [  
            e_id, 
           first_name, 
            last_name, 
            email, 
            phone_number, 
            hire_date, 
            job_id, 
            salary, 
            comission_pct, 
            manager_id, 
            department_id
            ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

    elif opt is "delete":
        e_id = data.get('id')
        sql = f"""delete from employees
        where employee_id = :id"""
        values = [e_id]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

    elif opt is "update":
        e_id = data.get('id')
        salary = data.get('salary')
        job = data.get('job_id')
        sql = f"""update employees 
        set salary = :salary, job_id = :job 
        where employee_id = :id;
        """
        values = [
            f"{salary}",
            f"{e_id}",
            f"{job}"
        ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

    else: #query
        e_id = data.get('id')
        # 
        sql = f"""select * 
        from employees 
        where employee_id = :id;
        """
        values = [f"{e_id}"]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

@app.route('/job')
def puesto():
    data = request.get_json()
    opt = data.get('opt')
    job_id = data.get('id')
    job_title = data.get('job_title')
    min_salary = data.get('min_salary')
    max_salary = data.get('max_salary')

    if opt is 'insert':
        sql = f"""insert into jobs 
            (
                job_id,
                job_title,
                min_salary,
                max_salary
            )
        values 
            (
                :job_id,
                :job_title,
                :min_salary,
                :max_salary
            )"""
        values = [  
            job_id, 
            job_title,
            min_salary, 
            max_salary, 
            ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

@app.route('/region')
def region():
    data = request.get_json()
    opt = data.get('opt')
    region_id = data.get('region_id')
    region_name = data.get('region_name')

    if opt is 'insert':
        sql = f"""insert into regions
            (
                region_id,
                region_name
            )
        values 
            (
                :region_id,
                :region_name
            )"""
        values = [  
            region_id, 
            region_name
            ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

@app.route('/country')
def region():
    data = request.get_json()
    opt = data.get('opt')
    country_id = data.get('country_id')
    country_name = data.get('country_name')
    region_id = data.get('region_id')

    if opt is 'insert':
        sql = f"""insert into countries 
            (
                country_id,
                country_name,
                region_id
            )
        values 
            (
                :country_id,
                :country_name,
                :region_id
            )"""
        values = [  
            country_id, 
            country_name,
            region_id
            ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())

@app.route('/location')
def region():
    data = request.get_json()
    opt = data.get('opt')
    location_id = data.get('location_id')
    street_adress = data.get('street_adress')
    postal_code = data.get('postal_code')
    city = data.get('city')
    state_province = data.get('state_province')
    country_id = data.get('country_id')
    

    if opt is 'insert':
        sql = f"""insert into locations 
            (
                location_id,
                street_adress,
                postal_code,
                city,
                state_province,
                country_id
            )
        values 
            (
                :location_id,
                :street_adress,
                :postal_code,
                :city,
                :state_province,
                :country_id
            )"""
        values = [  
            location_id, 
            street_adress,
            postal_code,
            city,
            state_province,
            country_id
            ]
        rs = cursor.execute(sql, values)
        print(rs.fetchall())


app.run(host= '0.0.0.0')
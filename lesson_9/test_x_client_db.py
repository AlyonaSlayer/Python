from lesson_9.Com_Emp_Table import CompanyTable
from lesson_9.Com_Emp_Table import EmployeeTable

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
com_db = CompanyTable(db_connection_string)
emp_db = EmployeeTable(db_connection_string)

def test_get_employee():
    employee_list = emp_db.get_employee_list()
    assert employee_list is not None

def test_add_new():
    name = 'Johnny'
    surname = 'Cage'
    midname = ''
    phone = '8999910291'
    email = 'cage@gmail.com'
    com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
    company_id = com_db.get_max_company_id()
    emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
    new_emp = emp_db.get_employee_max_id()
    employ = emp_db.get_employee_by_id(new_emp)
    emp_db.delete_employee(new_emp)
    com_db.delete_companies(company_id)
    assert employ[0][1] == True
    assert employ[0][4] == name
    assert employ[0][5] == surname
    assert employ[0][7] == phone

    
def test_update_employee():
    name = 'Johnny'
    surname = 'Cage'
    midname = ''
    phone = '8999910291'
    email = 'cage@gmail.com'
    com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
    company_id = com_db.get_max_company_id()
    emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
    new_emp = emp_db.get_employee_max_id()
    last_name = 'Blade'
    phone = '10312231'
    email = 'blade@outlook.com' 
    active = 'true'
    emp_db.update_employee(last_name, phone, email, active, new_emp)
    employ_up = emp_db.get_employee_by_id(new_emp)
    emp_db.delete_employee(new_emp)
    com_db.delete_companies(company_id)
    assert employ_up[0][5] == last_name
    assert employ_up[0][7] == phone
    assert employ_up[0][8] == email
    assert employ_up[0][1] == True
    
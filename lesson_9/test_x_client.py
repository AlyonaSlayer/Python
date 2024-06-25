from EmployeeAPI import EmployeeAPI
from Com_Emp_Table import CompanyTable
from Com_Emp_Table import EmployeeTable
db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
com_db = CompanyTable(db_connection_string)
emp_db = EmployeeTable(db_connection_string)
emp_api = EmployeeAPI("https://x-clients-be.onrender.com")

def test_create_company():
    list_last = com_db.get_active_companies()
    com_db.insert_new_company('AS','SA')
    list_after = com_db.get_active_companies()
    assert len(list_after) == len(list_last)+1 
    

def test_add_new_employee():
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

def test_get_employee_list():
    company_id = emp_api.get_active_company_id()
    resp_api = emp_api.get_employee_list(company_id)
    resp_db = emp_db.get_employee_list_in_company(company_id)
    assert len(resp_api) == len(resp_db)

def test_get_employee_list_missing_company_id():
    try:
        emp_api.get_employee_list()
    except TypeError as a:
        assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'id'"
    
def test_get_employee_list_invalid_company_id():
    try:
        emp_api.get_employee_list("")
    except TypeError as a:
        assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'id'"

def test_get_employee():
    name = 'Johnny'
    surname = 'Cage'
    midname = ''
    phone = '8999910291'
    email = 'cage@gmail.com'
    com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
    company_id = com_db.get_max_company_id()
    emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
    new_emp = emp_db.get_employee_max_id()
    employee_db = emp_db.get_employee_by_id(new_emp)
    employee_api = emp_api.get_employee_id(new_emp)
    emp_db.delete_employee(new_emp)
    com_db.delete_companies(company_id)
    assert employee_db[0][4] == employee_api['firstName']
    assert employee_db[0][5] == employee_api['lastName']
    assert employee_db[0][7] == employee_api['phone']
    assert employee_db[0][8] == employee_api['email']

def test_patch_employee():
    id = emp_api.get_active_company_id()
    name = 'Aly'
    surname = 'Bir'
    midname = 'Gal' 
    email = 'alybrgal@gmail.com'
    url = '' 
    phone = '123344556'
    new_employee = emp_api.create_new_employee(id, name, surname, midname, email, url, phone)['id']
    
    lastName = 'Ivan'
    email = 'Ivan@gmail.com' 
    url = ''
    phone = '89997776655'
    active = True
    patch_employee = emp_api.patch_employee(new_employee, lastName, email, url, phone, active)
    
    assert patch_employee.status_code == 200
    assert patch_employee.json()['id'] == new_employee
    assert patch_employee.json()['email'] == email
    assert patch_employee.json()['url'] == url
    assert patch_employee.json()['isActive'] == active
    
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





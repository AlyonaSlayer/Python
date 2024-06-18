import requests
from EmployeeAPI import EmployeeAPI
from CompanyAPI import CompanyAPI
import json


api = CompanyAPI("https://x-clients-be.onrender.com")
emp = EmployeeAPI("https://x-clients-be.onrender.com")
def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_create_company():
    body = api.get_company_list()
    len_before = len(body)
    result = api.create_company("Mortal Kombat 1", "Защита земного царства")
    new_id = result["id"]
    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == 'Mortal Kombat 1'
    assert body[-1]["description"] == 'Защита земного царства'
    assert body[-1]["id"] == new_id

def test_get_active_company():
    company_id = api.get_active_company_id()
    assert company_id is not None

def test_add_new_employee():
    id = api.get_active_company_id()
    name = 'Aly'
    surname = 'Bir'
    midname = 'Gal' 
    email = 'alybrgal@gmail.com'
    url = '' 
    phone = '123344556'

    new_employee = emp.create_new_employee(id, name, surname, midname, email, url, phone)
    assert new_employee is not None
    assert str(new_employee).isdigit() 

def test_get_employee_list():
    company_id = api.get_active_company_id()
    resp = emp.get_employee_list(company_id)
    assert resp is not None
    assert resp.status_code == 200

def test_get_employee_list_missing_company_id():
    try:
        emp.get_employee_list()
    except TypeError as a:
        assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'id'"
    
def test_get_employee_list_invalid_company_id():
    try:
        emp.get_employee_list("")
    except TypeError as a:
        assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'id'"

def test_get_employee():
    id = api.get_active_company_id()
    name = 'Aly'
    surname = 'Bir'
    midname = 'Gal' 
    email = 'alybrgal@gmail.com'
    url = '' 
    phone = '123344556'
    new_employee = emp.create_new_employee(id, name, surname, midname, email, url, phone)
    employee = emp.get_employee_id((new_employee['id']))
    assert employee is not None
    assert employee['id'] == new_employee['id']


def test_patch_employee():
    id = api.get_active_company_id()
    name = 'Aly'
    surname = 'Bir'
    midname = 'Gal' 
    email = 'alybrgal@gmail.com'
    url = '' 
    phone = '123344556'
    new_employee = emp.create_new_employee(id, name, surname, midname, email, url, phone)['id']
    
    lastName = 'Ivan'
    email = 'Ivan@gmail.com' 
    url = ''
    phone = '89997776655'
    active = True
    patch_employee = emp.patch_employee(new_employee, lastName, email, url, phone, active)
    
    assert patch_employee.status_code == 200
    assert patch_employee.json()['id'] == new_employee
    assert patch_employee.json()['email'] == email
    assert patch_employee.json()['url'] == url
    assert patch_employee.json()['isActive'] == active
    







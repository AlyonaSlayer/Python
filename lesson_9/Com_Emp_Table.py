from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable():
    __scripts = {
        "select" : text("select * from company"),
        "select active" : text("select * from company where \"is_active\" = true"),
        "select by id" : text("select * from company where id =:select_id"),
        "delete company" : text("delete from company where id = :id"),
        "insert_company" : text("insert into company(\"name\", \"description\") values (:new_name, :new_descr)"),
        "max_id" : text("select MAX(id) from company") 
    }
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string).connect()

    def get_companies(self):
        script = self.__db.execute(self.__scripts["select"]).fetchall()
        self.__db.commit()
        return script
    
    def get_active_companies(self):
        script = self.__db.execute(self.__scripts["select active"]).fetchall()
        self.__db.commit()
        return script

    def delete_companies(self, id):
        params = {
            "id" : id
            }
        script = self.__db.execute(self.__scripts["delete company"], params)
        self.__db.commit()
        return script
    
    def insert_new_company(self, new_name, new_descr):
        my_params = {
        "new_name" : new_name,
        "new_descr" : new_descr
        }
        script = self.__db.execute(self.__scripts["insert_company"], my_params)
        self.__db.commit()
        return script

    def get_max_company_id(self):
        script = self.__db.execute(self.__scripts["max_id"]).fetchall()[0][0]
        return script
    
    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], {"select_id" : id}).fetchall()
    
class EmployeeTable():
    __scripts = {
        "select" : text("select * from employee"),
        "insert new employee" : text("insert into employee (\"first_name\",\"last_name\",\"middle_name\",\"phone\",\"email\",\"company_id\") values (:name,:surname,:midname,:phone,:email,:id)"),
        "delete by id" : text("delete from employee where id = :id"),
        "select by company id" : text("select * from employee where \"company_id\" = :company_id"),
        "get_employee_max_id" : text("select MAX(id) from employee"),
        "get_employee_by_id" : text("select * from employee where id = :employee_id"),
        "update employee" : text("update employee set \"last_name\" = :last_name, \"phone\" = :phone, \"email\" = :email, \"is_active\" = :active where \"id\" = :id")
    }
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string).connect()

    def get_employee_list(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()
    
    def get_employee_list_in_company(self, company):
        params = {
            "company_id" : company
        }
        return self.__db.execute(self.__scripts["select by company id"], params).fetchall()
        
    
    def add_new_employee(self, name,surname,midname,phone,email,company_id):
        body = {
            "name" : name,
            "surname" : surname,
            "midname" : midname,
            "phone" : phone,
            "email" : email,
            "id" : company_id
        }
        script = self.__db.execute(self.__scripts["insert new employee"], body)
        self.__db.commit()

    def get_employee_by_id(self, employee_id):
        return self.__db.execute(self.__scripts["get_employee_by_id"], {"employee_id" : employee_id}).fetchall()
        
    def delete_employee(self, id):
        params = {
            "id" : id
            }
        self.__db.execute(self.__scripts["delete by id"], params)
        self.__db.commit()

    def get_employee_max_id(self):
        return self.__db.execute(self.__scripts["get_employee_max_id"]).fetchall()[0][0]
    
    def update_employee(self, last_name, phone, email, active, id):
        params = {
            "last_name" : last_name,
            "phone" : phone,
            "email" : email,
            "active" : active,
            "id" : id
        }
        self.__db.execute(self.__scripts["update employee"], params)
        self.__db.commit()
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure
class CompanyTable():
    """
            Этот класс взаимодействует с таблицей "Company" из базы данных
    """
    __scripts = {
        "select" : text("select * from company"),
        "select active" : text("select * from company where \"is_active\" = true"),
        "select by id" : text("select * from company where id =:select_id"),
        "delete company" : text("delete from company where id = :id"),
        "insert_company" : text("insert into company(\"name\", \"description\") values (:new_name, :new_descr)"),
        "max_id" : text("select MAX(id) from company") 
    }
    def __init__(self, connection_string):
        """
                Эта функция подключается к базе данных
        """
        self.__db = create_engine(connection_string).connect()
    
    @allure.step("Получить список компаний из таблицы Company")
    def get_companies(self) -> list:
        """
            Эта функция получет список компаний из таблицы
        """
        script = self.__db.execute(self.__scripts["select"]).fetchall()
        self.__db.commit()
        return script
    
    @allure.step("Получить список активных компаний из таблицы Company")
    def get_active_companies(self) -> list:
        """
                Эта функция получает список активных компаний из таблицы "Company"
        """
        script = self.__db.execute(self.__scripts["select active"]).fetchall()
        self.__db.commit()
        return script
    
    @allure.step("Удалить компанию по ID - {id} из таблицы Company")
    def delete_companies(self, id: int):
        """
                Эта функция удаляет компанию по номеру ID из таблицы "Company"
        """
        params = {
            "id" : id
            }
        self.__db.execute(self.__scripts["delete company"], params)
        self.__db.commit()
    
    @allure.step("Создать новую компанию в таблице Company")
    def insert_new_company(self, new_name:str, new_descr:str):
        """
                Эта функция создает новую компанию
                с двумя параметрами: Name и Description
                в таблице "Company"
        """
        my_params = {
        "new_name" : new_name,
        "new_descr" : new_descr
        }
        self.__db.execute(self.__scripts["insert_company"], my_params)
        self.__db.commit()
    
    @allure.step("Получить ID - {script} последней созданной компании в таблице Company")
    def get_max_company_id(self) -> int:
        """
                Эта функция возвращает ID последней созданной компании
                из таблицы "Company"
        """
        script = self.__db.execute(self.__scripts["max_id"]).fetchall()[0][0]
        return script
    
    @allure.step("Получить данные о компании по ее ID из таблицы Company")
    def get_company_by_id(self, id: int) -> list:
        """
                Эта функция получет данные компании,
                по нужному ID, из таблицы "Company"
        """
        return self.__db.execute(self.__scripts["select by id"], {"select_id" : id}).fetchall()
    
class EmployeeTable():
    """
            Этот класс взаимодействует с таблицей "Employee" из БД
    """
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
        """
                Эта функция подключается к базе данных
        """
        self.__db = create_engine(connection_string).connect()

    @allure.step("Получить список работников из таблицы Employee")
    def get_employee_list(self) -> list:
        """
                Эта функция возвращает список работников из таблицы "Employee"
        """
        return self.__db.execute(self.__scripts["select"]).fetchall()
    
    @allure.step("Получить список работников из компании по ID - {company} из таблицы Employee")    
    def get_employee_list_in_company(self, company:int) -> list:
        """
                Эта функция получает список работников одной компании
                из таблицы "Employee"
        """
        params = {
            "company_id" : company
        }
        return self.__db.execute(self.__scripts["select by company id"], params).fetchall()
    
    @allure.step("Создать сотрудника в таблице Employee")        
    def add_new_employee(self, name:str,surname:str,midname:str,phone:str,email:str,company_id:int):
        """
                Эта функция создает нового сотрудника в таблице "Employee"
        """
        body = {
            "name" : name,
            "surname" : surname,
            "midname" : midname,
            "phone" : phone,
            "email" : email,
            "id" : company_id
        }
        self.__db.execute(self.__scripts["insert new employee"], body)
        self.__db.commit()

    @allure.step("Получить информацию о сотруднике по его ID - {employee_id} из таблицы Employee")
    def get_employee_by_id(self, employee_id:int) -> list:
        """
                Эта функция возвращает информацию о сотруднике по его ID
        """
        return self.__db.execute(self.__scripts["get_employee_by_id"], {"employee_id" : employee_id}).fetchall()

    @allure.step("Удалить сотрудника по его ID - {employee_id} из таблицы Employee")
    def delete_employee(self, employee_id:int):
        """
                Эта функция удаляет сотрудника по номеру ID
                из таблицы "Employee"
        """
        params = {
            "id" : employee_id
            }
        self.__db.execute(self.__scripts["delete by id"], params)
        self.__db.commit()
    
    @allure.step("Получить ID - {emp} последнего созданного сотрудника из таблицы Employee")
    def get_employee_max_id(self) -> list:
        """
                Эта функция возвращает ID последнего сотрудника
                из таблицы "Employee"
        """
        emp = self.__db.execute(self.__scripts["get_employee_max_id"]).fetchall()[0][0]
        return emp
    
    @allure.step("Изменить данные сотрудника по его ID - {employee_id} в таблице Employee")
    def update_employee(self, last_name:str, phone:str, email:str, active:bool, employee_id: int):
        """
                Эта функция меняет данные сотрудника в таблице "Employee"
        """
        params = {
            "last_name" : last_name,
            "phone" : phone,
            "email" : email,
            "active" : active,
            "id" : employee_id
        }
        self.__db.execute(self.__scripts["update employee"], params)
        self.__db.commit()
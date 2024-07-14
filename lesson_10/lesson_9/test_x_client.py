from EmployeeAPI import EmployeeAPI
from Com_Emp_Table import CompanyTable
from Com_Emp_Table import EmployeeTable
import allure
@allure.epic("Урок 9. Тесты API и DataBase")
@allure.severity("blocker") 
class EmployeeTest:
    db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
    com_db = CompanyTable(db_connection_string)
    emp_db = EmployeeTable(db_connection_string)
    emp_api = EmployeeAPI("https://x-clients-be.onrender.com")
    
    @allure.id("Test_company_create")
    @allure.story("Создание новой компании")
    @allure.feature("Test_Company")
    @allure.title("Создание новой компании")
    @allure.description("Проверить создание компании и ее удаление из списка компаний")
    def test_create_company(self):
        list_last = self.com_db.get_active_companies()
        self.com_db.insert_new_company('AS','SA')
        new_comp = self.com_db.get_max_company_id()
        list_after = self.com_db.get_active_companies()
        self.com_db.delete_companies(new_comp)
        with allure.step("Проверить список компаний до создания и после"):
            assert len(list_after) == len(list_last)+1 

    @allure.id("Test_employee_add")
    @allure.story("Создание нового сотрудника")
    @allure.feature("Test_Employee")
    @allure.title("Создание нового сотрудника")
    @allure.description("Проверить создание нового сотрудника и удалить его из базы данных")
    def test_add_new_employee(self):
        name = 'Johnny'
        surname = 'Cage'
        midname = ''
        phone = '8999910291'
        email = 'cage@gmail.com'
        self.com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
        company_id = self.com_db.get_max_company_id()
        self.emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
        new_emp = self.emp_db.get_employee_max_id()
        employ = self.emp_db.get_employee_by_id(new_emp)
        self.emp_db.delete_employee(new_emp)
        self.com_db.delete_companies(company_id)
        with allure.step("Проверить данные нового сотрудника в БД"):
            assert employ[0][1] == True
            assert employ[0][4] == name
            assert employ[0][5] == surname
            assert employ[0][7] == phone

    @allure.id("Test_employee_get_list")
    @allure.story("Получение списка сотрудников компании")
    @allure.feature("Test_employee")
    @allure.title("Получить список сотрудников 1 компании")
    @allure.description("Проверить списки сотрудников 1 компании через API и DataBase")
    def test_get_employee_list(self):
        company_id = self.emp_api.get_active_company_id()
        resp_api = self.emp_api.get_employee_list(company_id)
        resp_db = self.emp_db.get_employee_list_in_company(company_id)
        assert len(resp_api) == len(resp_db)

    @allure.id("Test_get_employee_2")
    @allure.story("Проверить API запрос получения сотрудников без ID компании")
    @allure.feature("Test_employee")
    @allure.title("Проверить API запрос получения сотрудников без ID компании")
    def test_get_employee_list_missing_company_id(self):
        try:
            self.emp_api.get_employee_list()
        except TypeError as a:
            assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'company_id'"
    
    @allure.id("Test_get_employee_3")
    @allure.story("Проверить API запрос получения сотрудников с пустым ID компании")
    @allure.feature("Test_employee")
    @allure.title("Проверить API запрос получения сотрудников с пустым ID компании")
    def test_get_employee_list_invalid_company_id(self):
        try:
            self.emp_api.get_employee_list("")
        except TypeError as a:
            assert str(a) == "EmployeeAPI.get_employee_list() missing 1 required positional argument: 'id'"

    @allure.id("Test_employee_get_id")
    @allure.story("Получить информацию о сотруднике по его ID")
    @allure.feature("Test_employee")
    @allure.title("Получить информацию о сотруднике по его ID")
    @allure.description("Получить информацию о сторуднике по его ID через API запрос и из таблицы Employee и сравнить результат")
    def test_get_employee(self):
        name = 'Johnny'
        surname = 'Cage'
        midname = ''
        phone = '8999910291'
        email = 'cage@gmail.com'
        self.com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
        company_id = self.com_db.get_max_company_id()
        self.emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
        new_emp = self.emp_db.get_employee_max_id()
        employee_db = self.emp_db.get_employee_by_id(new_emp)
        employee_api = self.emp_api.get_employee_id(new_emp)
        self.emp_db.delete_employee(new_emp)
        self.com_db.delete_companies(company_id)
        with allure.step("Проверить данные сотрудника в БД и через API запрос"):
            assert employee_db[0][4] == employee_api['firstName']
            assert employee_db[0][5] == employee_api['lastName']
            assert employee_db[0][7] == employee_api['phone']
            assert employee_db[0][8] == employee_api['email']

    @allure.id("test_patch_employee_api")
    @allure.story("Изменить данные сотрудника по его ID через API запрос")
    @allure.feature("Test_employee")
    @allure.title("Изменить данные сотрудника по его ID - {new_employee} через API запрос")
    @allure.description("Создать сотрудника в компании, заменить данные сотрудника и проверить изменения")
    def test_patch_employee(self):
        self.com_db.insert_new_company("As","desc")
        id = self.com_db.get_max_company_id()
        name = 'Aly'
        surname = 'Bir'
        midname = 'Gal' 
        email = 'alybrgal@gmail.com'
        url = '' 
        phone = '123344556'
        new_employee = self.emp_api.create_new_employee(id, name, surname, midname, email, url, phone)['id']
    
        lastName = 'Ivan'
        email = 'Ivan@gmail.com' 
        url = ''
        phone = '89997776655'
        active = True
        patch_employee = self.emp_api.patch_employee(new_employee, lastName, email, url, phone, active)
        self.emp_db.delete_employee(new_employee)
        self.com_db.delete_companies(id)
        with allure.step("Проверить измененные данные сотрудника через API запрос"):
            assert patch_employee['id'] == new_employee
            assert patch_employee['email'] == email
            assert patch_employee['url'] == url
            assert patch_employee['isActive'] == active
    
    @allure.id("Test_employee_update_db")
    @allure.story("Измеить данные сотрудника по его ID в таблице Employee")
    @allure.feature("Test_employee")
    @allure.title("Измеить данные сотрудника по его ID - {new_emp} в таблице Employee")
    @allure.description("Создать сотрудника и изменить его данные и проверить результат в БД")
    def test_update_employee(self):
        name = 'Johnny'
        surname = 'Cage'
        midname = ''
        phone = '8999910291'
        email = 'cage@gmail.com'
        self.com_db.insert_new_company('Mortal Kombat', 'Shao Kan')
        company_id = self.com_db.get_max_company_id()
        self.emp_db.add_new_employee(name, surname, midname, phone, email, company_id)
        new_emp = self.emp_db.get_employee_max_id()
        last_name = 'Blade'
        phone = '10312231'
        email = 'blade@outlook.com' 
        active = 'true'
        self.emp_db.update_employee(last_name, phone, email, active, new_emp)
        employ_up = self.emp_db.get_employee_by_id(new_emp)
        self.emp_db.delete_employee(new_emp)
        self.com_db.delete_companies(company_id)
        with allure.step("Проверить измененные данные сотрудника в БД"):
            assert employ_up[0][5] == last_name
            assert employ_up[0][7] == phone
            assert employ_up[0][8] == email
            assert employ_up[0][1] == True





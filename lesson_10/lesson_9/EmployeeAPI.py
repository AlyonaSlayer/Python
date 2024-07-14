import requests
import allure
class EmployeeAPI:
    """
            Этот класс взаимодействет с сайтом через API запросы
    """
    def __init__(self, url:str):
        """
                Эта функция передает Url сайта для дальнейших API запросов
        """
        self.url = url
    
    @allure.step("Получить токен через API запрос")
    def get_token(self, user='flora', password='nature-fairy'):
        """
                Эта функция получает авторизованный токен
        """
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']
    
    @allure.step("Создать компанию через API запрос")
    def create_company(self, name:str, description:str) -> dict:
        """
                Эта функция создает новую компанию через API запрос
        """
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()
    
    @allure.step("Получить список компаний через API запрос")
    def get_company_list(self, params_to_add=None) -> list:
        """
                Эта функция получает список компаний через API запрос
        """
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    @allure.step("Получить ID - {com_id} через API запрос")
    def get_active_company_id(self, my_params = {'is_active' : 'true'}) -> int:
        """
                Эта функция возвращает последнюю компанию
                из списка активных компаний через API запрос
        """
        resp = requests.get(self.url + '/company', params=my_params)
        com_id = resp.json()[-1]['id']
        return com_id
    
    @allure.step("Получить список сотрудников компании по ID - {company_id} через API запрос")
    def get_employee_list(self, company_id: int) -> list:
        """
                Эта функция возвращает список сотрудников из компании
                через API запрос
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        company = {'company' : company_id}

        list = requests.get(self.url + '/employee',
                             headers=my_headers, params=company)
        return list.json()
    
    @allure.step("Создать нового сотрудника в компании по ее ID - {company_id} через API запрос")
    def create_new_employee(self, company_id:int, name:str, surname:str, midname:str, email:str, url:str, phone:str) -> dict:
        """
                Эта функция создает нового сотрудника в компании через API запрос
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        body = {
            "id": 0,
            "firstName": name,
            "lastName": surname,
            "middleName": midname,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": True
        }

        resp = requests.post(self.url + '/employee', headers=my_headers, json=body)
        return resp.json()
    
    @allure.step("Получить данные о сотруднике по его ID - {employee_id} через API запрос")
    def get_employee_id(self, employee_id: int) -> dict:
        """
                Эта функция возвращает данные о сотруднике по его ID
                через API запрос
        """
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    
    @allure.step("Изменить данные сотрудника по его ID - {employee_id} через API запрос")
    def patch_employee(self, employee_id: int, lastName:str, email:str, url:str, phone:str, active:bool) -> dict:
        """
                Эта функция меняет данные сотрудника по его ID через API запрос
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        body = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": active
        }
        resp = requests.patch(self.url + '/employee/' + str(employee_id), headers=my_headers, json=body)
        return resp.json()
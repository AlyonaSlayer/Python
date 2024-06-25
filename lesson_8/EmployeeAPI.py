import requests
import json
class EmployeeAPI:
    def __init__(self, url):
        self.url = url

    def get_token(self, user='flora', password='nature-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']
    
    def create_company(self, name, description):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()
        
    def get_employee_list(self, id: int):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        company = {'company' : id}

        list = requests.get(self.url + '/employee',
                             headers=my_headers, params=company)
        return list
    
    def create_new_employee(self, id, name, surname, midname, email, url, phone):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        body = {
            "id": 0,
            "firstName": name,
            "lastName": surname,
            "middleName": midname,
            "companyId": id,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": True
        }

        resp = requests.post(self.url + '/employee', headers=my_headers, json=body)
        return resp.json()
    
    def get_employee_id(self, id: int):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    def patch_employee(self, id: int, lastName, email, url, phone, active):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        body = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": active
        }
        resp = requests.patch(self.url + '/employee/' + str(id), headers=my_headers, json=body)
        return resp
from selenium.webdriver.common.by import By


class DataFild():
    def __init__(self, driver):
        self._driver = driver
        
    def find_fields(self):
        self._first_name_id = ("first-name")
        self._last_name_id = ("last-name")
        self._address_id = ("address")
        self._zip_code_id = ("zip-code")
        self._city_id = ("city")
        self._country_id = ("country")
        self._email_id = ("e-mail")
        self._phone_number_id = ("phone")
        self._job_position_id = ("job-position")
        self._company_id = ("company")

    def get_class_first_name(self):
        return self._driver.find_element(By.ID,self._first_name_id).get_attribute("class")
    
    def get_class_last_name(self):
        return self._driver.find_element(By.ID,self._last_name_id).get_attribute("class")

    def get_class_address(self):
        return self._driver.find_element(By.ID,self._address_id).get_attribute("class")

    def get_class_zip_code(self):
        return self._driver.find_element(By.ID,self._zip_code_id).get_attribute("class")

    def get_class_city(self):
        return self._driver.find_element(By.ID,self._city_id).get_attribute("class")
    
    def get_class_country(self):
        return self._driver.find_element(By.ID,self._country_id).get_attribute("class")
    
    def get_class_email(self):
       return self._driver.find_element(By.ID,self._email_id).get_attribute("class")

    def get_class_phone_number(self):
        return self._driver.find_element(By.ID,self._phone_number_id).get_attribute("class")
    
    def get_class_job_position(self):
        return self._driver.find_element(By.ID,self._job_position_id).get_attribute("class")

    def get_class_company(self):
        return self._driver.find_element(By.ID,self._company_id).get_attribute("class")
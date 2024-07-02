from selenium.webdriver.common.by import By


class DataFild():
    """
            Этот класс позволяет получить информацию со страницы с заполненными данными
    """
    def __init__(self, driver):
        """
                Инициализирует вебдрайвер
        """
        self._driver = driver
      
    def find_fields(self):
        """
                Эта функция запоминает локаторы для дальнейшего использования
        """
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
        """
                Данная функция возвращает атрибут класса в поле "Имя"
        """
        return self._driver.find_element(By.ID,self._first_name_id).get_attribute("class")
    
    def get_class_last_name(self):
        """
                Данная функция возвращает атрибут класса в поле "Фамилия"
        """
        return self._driver.find_element(By.ID,self._last_name_id).get_attribute("class")
    
    def get_class_address(self):
        """
                Данная функция возвращает атрибут класса в поле "Адрес"
        """
        return self._driver.find_element(By.ID,self._address_id).get_attribute("class")
    
    def get_class_zip_code(self):
        """
                Данная функция возвращает атрибут класса в поле "Зип код"
        """
        return self._driver.find_element(By.ID,self._zip_code_id).get_attribute("class")
    
    def get_class_city(self):
        """
                Данная функция возвращает атрибут класса в поле "Город"
        """
        return self._driver.find_element(By.ID,self._city_id).get_attribute("class")
    
    def get_class_country(self):
        """
                Данная функция возвращает атрибут класса в поле "Страна"
        """
        return self._driver.find_element(By.ID,self._country_id).get_attribute("class")
    
    def get_class_email(self):
        """
                Данная функция возвращает атрибут класса в поле "Почта"
        """
        return self._driver.find_element(By.ID,self._email_id).get_attribute("class")
    
    def get_class_phone_number(self):
        """
                Данная функция возвращает атрибут класса в поле "Телефон"
        """
        return self._driver.find_element(By.ID,self._phone_number_id).get_attribute("class")
    
    def get_class_job_position(self):
        """
                Данная функция возвращает атрибут класса в поле "Место работы"
        """
        return self._driver.find_element(By.ID,self._job_position_id).get_attribute("class")
    
    def get_class_company(self):
        """
                Данная функция возвращает атрибут класса в поле "Компания"
        """
        return self._driver.find_element(By.ID,self._company_id).get_attribute("class")
    
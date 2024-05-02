class User:
    
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name
        
    def sayName(self):
        print(self.name)

    def saySurname(self):
        print(self.surname)
    
    def sayFNLN(self):
        print(self.name, self.surname)
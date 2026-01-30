class Employee:
    company = "ITC"
    def show(self):
        print(f" The name of th employee is {self.name} and the salary is {self.salary}")
        
class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and good with {self.language} language")
        
a= Employee()
b= Programmer()
print(a.company,b.company)
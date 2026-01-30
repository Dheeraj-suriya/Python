class Employee:
    company = "ITC"
    name = "Dheeraj"
    def show(self):
        print(f" The name of th employee is {self.name} and the company is {self.company}")
        
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all Language here is your language: {self.language}")
        
class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and good with {self.language} language")
        
a= Employee()
b= Programmer()

b.show()
b.printLanguage()
b.showLanguage()
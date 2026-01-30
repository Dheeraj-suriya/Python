class Employee:
    language="Python"  
    salary=1200000
    
    def __init__(self,name,salary,language): # it is called as DUNDER METHOD which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
    
Dheeraj = Employee("dheeraj",1200000, "Javascript")
# Dheeraj.language="Javascript"
Dheeraj.name="dheeraj"  
print(Dheeraj.name,Dheeraj.language, Dheeraj.salary)


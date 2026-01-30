class Employee:
    a = 1
    
    @classmethod  
    def show(cls):
        print(f"The class attribute of a is: {cls.a}")
        
e=Employee()
e.a = 45
e.show()

# if " @classmethod is not used it considers instance attribute e.a = 45, 
# else if used, it ignores instance attribut and prints class attribut as 1"
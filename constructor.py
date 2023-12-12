

    # 1. Class Defination
class Parent():


    #1.1 Property= Varible
    Bloodgroup= "" # define Property


    #1.2 Constructor is a special function/Method
    def __init__(self):
        self.Bloodgroup= "O+ve" # Property Value Intialization


    #1.3 Method = Function
    def myMethod(self):
        print(f"My Blood Group Is {self.Bloodgroup}")


    #2.Create Class Object
ceo = Parent()

    #2.1 Call Method with Class Object    
ceo.myMethod()
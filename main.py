class Employee:
    def __init__(self):
        print("Employee called.")
    def __del__(self):
        print("Destructor called.Employee deleted.")
    
obj=Employee()
del obj
    
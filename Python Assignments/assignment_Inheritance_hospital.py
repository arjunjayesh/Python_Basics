"""
Parent Class: Hospital -> admin, doctor, nurse, dept
2nd Class: Dept -> Displays admin, doctor, nurse, dept
3rd class: Patientward -> patient details such as name,age,num and display
"""
class Hospital:
    def __init__(self,admin,doctor,nurse,dept):
        self.admin=admin
        self.doctor=doctor
        self.nurse=nurse
        self.dept=dept
    def get_info(self):
        self.admin=input("Enter the Admin Info: ")
        self.doctor=input("Enter the Name of the Doctor: ")
        self.nurse=input("Enter the Name of the Nurse: ")
        self.dept=input("Enter the Name of the Department: ")
class Department(Hospital):
    def display(self):
        print(self.admin, self.doctor, self.nurse, self.dept)
class Patient():
    def get_info(self, pname, age, pno):
        self.pname=input("Enter the Name of the Patient: ")
        self.age=int(input("Enter the Age of the Patient: "))
        self.pno=input("Enter the Phone Number of the Patient: ")
    def display(self):
        print(self.pname, self.age, self.pno)
obj1=Department('','','','')
obj2=Patient()
obj1.get_info()
obj2.get_info('','','')
obj1.display()
obj2.display()
class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def get_details(self):
        self.name=input("Enter Your Name: ")
        self.mark=int(input("Enter Your Marks: "))
    def put_details(self):
        print(self.name,self.mark)

class Teacher(Student): # Teacher class inherits Student Class
    def display(self):
        print("I am Derived Class")

class Parent(Teacher): # Parent CLass Inherits Student Class
    def newfun(selfself):
        print("I am Derived Class 2")

class Admin(Parent): # Admin Class Inherits Teacher Class
    def funadmin(self):
        print("I am Admin")

obj=Admin('','')
obj.get_details()
obj.put_details()
obj.display()
obj.funadmin()

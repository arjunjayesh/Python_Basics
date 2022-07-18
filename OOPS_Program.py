class Student:
    def __init__(self,name,mark): #self is used to refer the current instance of a class
        self.name=name
        self.mark=mark
    def get_details(self):
        self.name=input("Enter your Name: ")
        self.mark=int(input('Enter your Marks: '))
    def put_details(self):
        print(self.name,self.mark)
obj=Student('','')
obj.get_details()
obj.put_details()
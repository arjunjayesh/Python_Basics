"""
Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.
Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
You can use any specifications which you want. The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.

Make sure that the sub classes have their own methods to get and display their special specification.

Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.

Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.

You can use any specifications which you want. The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.

Make sure that the sub classes have their own methods to get and display their special specification.

Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class

"""

class Computer:
    def __init__(self,processor,memory,storage):
        self.processor=processor
        self.memory=memory
        self.storage=storage

    def getspecs(self):
        self.processor=input("Processor: ")
        self.memory=input("RAM: ")
        self.storage=input("HDD / SSD: ")

    def displayspecs(self):
        print("Processor: ",self.processor)
        print("RAM: ",self.memory)
        print("SSD / HDD Capacity",self.storage)

class Laptop(Computer):
    def lapspecs(self):
        self.weight=input("Enter the Laptop Weight: ")

    def displaylapspecs(self):
        print("Laptop Weight: ",self.weight)

class Desktop(Computer):
    def deskspecs(self):
        self.monitorsize=input("Enter the monitor screen size: ",self.monitorsize)

    def displaydeskspecs(self):
        print("Desktop Screen Size:", self.monitorsize)

x=input("Laptop or Desktop? : ")

if x=="Laptop":
    lap = Laptop('', '', '')
    lap.getspecs()
    lap.lapspecs()
    lap.displayspecs()
    lap.displaylapspecs()

elif x=="Desktop":
    desk = Desktop('', '', '')
    desk.getspecs()
    desk.deskspecs()
    desk.displayspecs()
    desk.displaydeskspecs()

else:
    print("Invalid Selection")





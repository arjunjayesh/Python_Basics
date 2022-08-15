file=open("Demo.txt",'r') # Reading a file
content=file.read()
print(content)
file.close()

file=open("Demo.txt",'w') # Replaces and Writes over existing
file.write("I am Python Django")
file.close()

file=open("Demo.txt",'a') # Appends to the existing content
file.write("\nI am append")
file.close()
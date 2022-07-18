"""
1. Write Python code to open a file named demo.txt and write some random data into it.
2. Open the file, read the contents and display them as output.
3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.

"""
file=open("Demo.txt",'w') # Creating a new file
file.close()

file = open("Demo.txt", 'w')  # Creating a new file
file.write("I am Writing to a Blank file as reading a blank file returns an error")
file.close()

file = open("Demo.txt", 'r')  # Reading a file
content = file.read()
print(content)
file.close()

file=open("Demo.txt",'w') # Replaces and Writes over existing
file.write("I am Writing over the previous content")
file.close()

file=open("Demo.txt",'a') # Appends to the existing content
file.write("\nI am appending new content without removing the previous content")
file.close()
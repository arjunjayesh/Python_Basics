# Create list and create a new list from the existing list

list1=[9,7,5,21,22,45,65,74,96,85,14,35,36,66,64]

rev=list1[::-1] #Reverse of list1
print("Reverse of the List: ", rev)

# Create integer list and print index 2 to 6

print("Items at Index 2 to 6: ", list1[2:7]) # Print items at index 2 to 6

# Create tuple; append and insert elements, index of second last index

x=(5,9,8,12,65,44,17)
print("Tuple X: ", x)

y=list(x) # Convert tuple x to list y
print("List y: ", y)
y.insert(2,"New Item") # Insert "New Item" at index 2 of list y
y.append("Last Item") # Append "Last Item" at last index of list y
print("List y: ", y)
print(type(y))

x=tuple(y) # Convert list y to tuple x
print("Tuple X: ", x)
print(type(x))

length=len(x) # Length of the tuple x
print(x[length-2]) # Prints item at second last index of the tuple
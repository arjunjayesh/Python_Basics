list1=[22,33,"Hello","Python"]
print(list1)
print(list1[0])
print(list1[1])

# Forward Indexing Starts at 0
# Reverse Indexing Starts at 1

print(list1[-1]) # Reverse Indexing

print(len(list1)) # Returns length of the list

print(type(list1)) # Returns the data type of the list

list2 = list(("django","flask","pyramid"))
print(list2)
print(type(list2))

print(list1+list2) # Output will be a single list

# Swapping Value in a list
print(list2)
list2[1]="Hello"
print(list2)

fruits=["apple","orange","pineapple"]
print(fruits)
fruits.append("cherry") # append adds item at the end of the list
print(fruits)

fruits.insert(1,"Grapes") # insert adds item at the specified index
print(fruits)

print(fruits.index("cherry")) # index of item in the list

fruits.remove(("orange")) # remove item from list
print(fruits)

fruits.pop(1) # removes item at index
print(fruits)

del fruits[0] # delete item at index
print(fruits)

fruits.clear() # removes all items from the list
print(fruits)

# Slice Operations

x=[20,30,40,10,50,9,8,5,0,4,3]
print(x)
print(x[2:7]) # Slices from Index 2 to 7
print(x[2:7:2]) # Slices from Index 2 to 7 at 2 intervals
print(x[::-1]) # Reverse the list

result=[]
for i in "inmakes":
    result.append(i)
print(result)

# List Comprehensive
# expression loop condition

result = [i for i in "inmakes"] # List Comprehensive
print(result)

result=["Python","Django","Flask","People"]
new=[i for i in result if 'P' in i]
print(new)

new=[i for i in range(10)]
print(new)

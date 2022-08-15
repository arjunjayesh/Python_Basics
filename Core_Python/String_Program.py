# String Functions

li=[10,20,30,40]
newstring="my numbers:{0}{1}{2}".format(li[1],li[3],li[0])
print(newstring)
newstring="my numbers:{0}, {1}, {2}".format(li[1],li[3],li[0])
print(newstring)
newlist=[{0},{1}]
print(newlist)
print(type(newlist))

newstring1="Hello, I am Inmakes"
print(newstring1.upper())
print(newstring1.lower())
print(newstring1.startswith("p"))
print(newstring1.endswith("s"))

# Numeric Functions

print(min(1,2,3,5,4,9,8))
print(max(22,44,11,33,126))
print(abs(-788)) # used to get positive numbers of it's corresponding negative number


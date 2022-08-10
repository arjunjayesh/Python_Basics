"""
Create a set with 6-7 elements
-> Add element
-> remove element
-> difference in two sets
"""
numbers={1,2,3,4,8,9,10,6,5,4,3,2}
print(numbers)

numbers.add(11)
print(numbers)

numbers.remove(10)
print(numbers)

seta={1,2,3,4,5,2,7,9,1}
setb={4,5,6,7,8,2,3}
print(seta | setb) # Union
print(seta & setb) # Intersection
print(seta - setb) # Difference
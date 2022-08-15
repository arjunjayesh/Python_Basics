# Syntax: Dict = {key:value,}
x={
    "chair":500,
    "table":300,
    34:"Python"
}
print(x)
print(type(x))
print(x["chair"])
print(len(x)) # Length

x["veg"]=120 # Adding item to dictionary
print(x)

x.update({12:"Django"}) # Adding item to Dictionary
print(x)

x.pop("table") # Remove specific item
print(x)

x.popitem() # Removes last item
print(x)

print("\nKeys:")
for i in x: #Display keys
    print(i)

print("\nValues:")
for i in x.values():  # Display Values
    print(i)

print("\nKeys and Values:")
for i in x.items():  # Display Keys and its Values
    print(i)

# get function
print(x.get(1,"Key Not Found")) # 1 not in key list, hence returns message
print(x.get("veg","Key Not Found")) #key found
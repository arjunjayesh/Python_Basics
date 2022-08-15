import re
pattern="python"

if re.match(pattern,"Inmakespythonprogram"): # Satisfied Only if at the beginning
    print("Matched in match")
elif re.search(pattern, "Inmakespythonprogram"):
    print("Matched in search")
else:
    print("Not Matched")

print(re.findall(pattern,"Hello, I am python, python is a future tech, python is one")) # finds all

new=re.sub(pattern,"Inmakes","hai, I am python") # find and replace, python is replaced with Inmakes
print(new)

if re.match("r.d","rqd"):
    print("Correct")
else:
    print("Not Correct")

pattern="[A-Z][0-9][a-z]" # Character Class
if re.search(pattern,"p8u"):
    print("Matched")
else:
    print("Not Matched")
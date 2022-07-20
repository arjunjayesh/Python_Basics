import re
pattern="python"
if re.match(pattern,"Inmakespythonprogram"): # Satisfied Only if at the beginning
    print("Matched in match")
elif re.search(pattern, "Inmakespythonprogram"):
    print("Matched in search")
else:
    print("Not Matched")
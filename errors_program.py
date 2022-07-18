try:
    a=[12,34,56,78]
    print(a[4])
except: # Executed only when an error occurs
    print("There is a division Error")
finally: # Executed irrespective  of error
    print("I am Finally")

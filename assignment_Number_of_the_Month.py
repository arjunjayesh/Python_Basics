# Program to print Month of the Year

def month_calc(a):
    if a==1:
        return "January"
    elif a==2:
        return "February"
    elif a==3:
        return "March"
    elif a==4:
        return "April"
    elif a==5:
        return "May"
    elif a==6:
        return "June"
    elif a==7:
        return "July"
    elif a==8:
        return "August"
    elif a==9:
        return "September"
    elif a==10:
        return "October"
    elif a==11:
        return "November"
    elif a==12:
        return "December"
    else:
        return "Invalid Entry! There are only 12 Months in a year"

x=int(input("Enter the Number of the Month: "))
print("The Number you have Entered is ", x, "and the corresponding month is", month_calc(x))
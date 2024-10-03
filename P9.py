def miles():
    try:
        m=float(input("enter miles:"))
        k=m * 1.609344
        print('kilometers is',k)
    except:
        print('unknown')
def fahrenheit():
    try:
        f=float(input("enter fahrenheit:"))
        c=(f-32)*5/9
        print ('celsius is' , c)
    except:
        print('unknown')
def pounds():
    try:
        lb=float(input("enter pounds:"))
        kg=lb*0.45359237
        print("kilogram is", kg)
    except:
        print('unknown')
  
def main():
    ans="yes"
    while ans=="yes":
        miles()
        fahrenheit()
        pounds()
        ans=input('enter yes or no')


main()



            

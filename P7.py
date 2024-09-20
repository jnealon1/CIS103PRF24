def miles():
    m=float(input("enter miles:"))
    k=m * 1.609344
    print('kilometers is',k)
    return
def fahrenheit():
    f=float(input("enter fahrenheit:"))
    c=(f-32)*5/9
    print ('celsius is' , c)
def pounds():
    lb=float(input("enter pounds:"))
    kg=lb*0.45359237
    print("kilogram is", kg)
    return


def main():
    miles()
    fahrenheit()
    pounds()


                  
    

main()
print('done')
    
    

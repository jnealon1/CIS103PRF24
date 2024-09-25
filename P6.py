ans="y"
burn=4.9
while(ans=="y") or (ans=="y"):
    rt=5
    print(" calorie calculation")
    print("----------------")
    run=(input("enter running time in minutes"))
    if(len(run)==0 or run.isspace() or float(run)<5):
        print("input cannot blank or less than 5")
    else:
        run=float(run)

        while(rt<run+1):
                burncal=rt*burn
                print('minutes:' ,rt, 'burns:',burncal, 'calories')
                rt=rt+5
    ans=input("\nAgain y/n? ->")
print ("done")
        

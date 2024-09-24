print("--Program Start")
print("Table code: A=add, S=Subtract, M=multiple, D=Divide")
code=input("enter code")
number=float(input("enter a number"))
if code=="A" or code== "a":
    for x in range (1,11,1):
        answer=number + x
        print(answer, "=",number,"+",x)

else:
    if code=="S" or code== "s":
        for x in range (1,11,1):
            answer=number - x
            print(answer, "=",number, "-",x)

    else:
        if code== "M" or code== "m":
            for x in range (1,11,1):
                answer=number * x
                print(answer, "=", number, "*", x)

        else:
            if code== "D" or code== "d":
                for x in range (1,11,1):
                    answer=number / x
                    print(answer, "=", number, "/", x)
print("program done")
                    

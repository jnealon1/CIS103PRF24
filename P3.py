P=float(input('enter number of pounds '))
GS= P*0.99
print('Gross sales is ' , GS )
Discount=0
if (P>=10)  and  (P<99.99):
    Discount=0.1
    print('discount ', Discount)
else:
    if(P>=100) and (P<999.99):
        Discount=0.2
        print('discount ', Discount)
    else:
        if (P>=1000) and (P<9999.99):
            Discount=0.3
            print('discount ', Discount)
        else:
            if(P>=10000):
                Discount=0.4
                print('discount ', Discount)
DiscountAmount=GS*Discount
FinalAmount=GS-DiscountAmount
print('Discount:', DiscountAmount)
print('Final Amount:' , FinalAmount)

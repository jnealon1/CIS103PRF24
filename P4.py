name=input('enter a name')
lenstr= len(name)
if(lenstr ==0):
    print('name can not be blank')
else:
    if name.isspace():
        print('name can not be spaces')
    else:
        if lenstr<3:
            print('must be 3 characters long')
        else:
            if name.isalpha():
                print ('valid')
            else:
                print('must be alphabetic' )
#----------------------------------------
account=input('enter a account number')
lenacc=len (account)
if (lenacc ==0):
    print ('account number can not be blank')
else:
    if account.isspace():
        print('account can not have spaces')
    else:
        if lenacc!=9:
            print ('account number must be 9 digits ')
        else:
            if account.isnumeric():
                print ('valid')
            else:
                print ('account must be numeric')
#-------------------------------------
amount=input('enter payment amount')
lenamt=len (amount)
if lenamt ==0:
    print ('payment can not be blank')
else:
    if amount.isspace ():
        print('account can not have spaces')
    else:
        amt=float(amount)
        if amt==0:
            print ('account can not be zero' )
        else:
            if amt< 0:
                print ('account can not be negative')
            else:
                print ('valid')
            
















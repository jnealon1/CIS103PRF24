#import sys
#sys.setrecursionlimit(5000)    #(this sets the recursion so the program will not crash)

def fact (n):
    print(n,' ', end='')
    if n==1:
        return n
    else:
        
        return n + fact(n-1)


def main():
    ans='y'
    while ans.upper()== 'Y':
        print('Sum Up Numbers')
        numb=input('Enter a number')
        if numb== '':
            print('input cannot be blank')

        try:
            numb=int(numb)
            if numb <0:
                print('input cannot be negative')
                return
            

            a=fact(numb)
            print(numb, 'Sum is' ,a)
        
        except:
            print('input must be a number')

        ans=input('Again y/n:')
        print('Done')

                    


       





main()

    

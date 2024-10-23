#Jacquetta Nealon Fall 24' 10/22/2024
def main():
    dtr = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X', 11:'XI', 12:'XII', 13:'XIII', 14:'XIV', 15:'XV', 16:'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX', 21: 'XXI',
        22: 'XXII', 23: 'XXIII', 24: 'XXIV'}
    print('Dictionary example')
    print(dtr)



    a=int(input('enter a number:'))
    while a>0:
        if a in dtr:
            v01=dtr[a]
            print(a, 'Roman Numerial is',v01)
                        
        else:
            print(a, 'not in dictionary')
            print(a, 'Would you like to add it?')
            ans= input('y/n')
            if ans=='y':
               avalue=input('Enter value for key:')
               dtr[a]=avalue
               print('------')

                
                
                   

            
        a=int(input('enter a number:'))
    print('Program Done')      
main()
     

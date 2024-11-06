print('Rainfall for Chicago (2017):')
num=[0]*12
for x in range (0,12):
    print(x)
    num[x]= float(input('Enter Rainfall:'))


len01=len(num)
print(num)
print('Highest rainfall->', max(num))
print('Lowest rainfall->', min (num))
print('Total rainfall->', sum(num))
a=sum(num)/12
print('Average is', a)

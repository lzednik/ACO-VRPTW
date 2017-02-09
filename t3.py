#n1=[1,1,1,1,1,1,1,1,1,1]

n2=[[1]*10 for n in range(10)]



for n in n2:
    print(n)

n2[3][4]=20

print('')
print('')
print('')


for n in n2:
    print(n)



print('**************************************************')

print(n2[3])
print(n2[3][4])

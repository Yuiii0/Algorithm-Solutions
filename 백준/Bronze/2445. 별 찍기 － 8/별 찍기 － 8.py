n=int(input())

for i in range(1,n+1):
    print('*'*i,end='') #별
    print((' '*(n-i))*2,end='')   #공백
    print('*'*i)


for j in range(n-1, 0, -1):
    print('*'*j,end='')
    print((' '*(n-j))*2,end='')
    print('*'*j)

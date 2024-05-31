n=int(input())

total=0
temp=0
#i는 1부터 n-2 순회
for i in range(1,n-1): 
    temp=temp+i #1 3 6 

    total+=temp #1 4 10
    

print(total)
print(3)
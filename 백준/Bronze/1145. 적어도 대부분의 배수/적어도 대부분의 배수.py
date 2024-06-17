import sys
input=sys.stdin.readline

num_list=list(map(int,input().rstrip().split()))
min_value=min(num_list)

while True:
    count=0
    for num in num_list:
        if min_value%num==0:  
            count+=1
    if count>=3:
        break
    min_value+=1
print(min_value)
    

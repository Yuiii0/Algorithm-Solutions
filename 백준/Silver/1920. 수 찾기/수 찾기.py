import sys 

dict={}
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
for num in num_list:
    dict[num]=1 #1이면 존재한다는 의미
    
m=int(input())
num2_list=list(map(int,input().split()))
for num in num2_list:
    print(dict.get(num,0))
    

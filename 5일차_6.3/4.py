# X를 기준으로 누울수 있는 영역을 나눈다 (split) -> 2이상이면 카운트

import sys
input=sys.stdin.readline

n=int(input())
row=0
col=0

rooms=[]

#가로 
for i in range(n):
    x_list=input().rstrip()
    rooms.append(list(x_list))
    row+=len(list(filter(lambda x:len(x)>=2,x_list.split('X'))))

#세로
for i in range(n):
    temp=''
    for j in range(n):
        temp+=rooms[j][i]
    col+=len(list(filter(lambda x:len(x)>=2,temp.split('X'))))     
       
        
print(row,col)

#31120	44
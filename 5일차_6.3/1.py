import sys
input=sys.stdin.readline

n,m=map(int,input().split())

#A 생성
a_list=[]
for _ in range(n):
    x_list=list(map(int,input().split()))
    a_list.append(x_list)

#B 생성
b_list=[]
for _ in range(n):
    x_list=list(map(int,input().split()))
    b_list.append(x_list)


#result 리스트 생성
result=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j]=a_list[i][j]+b_list[i][j]

#출력
for r in result:
    print(" ".join(map(str, r)))
  

#31120 48
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
num=min(a,b)

#배열 생성
l=[]
for i in range(a):
    l.append(list(input().rstrip()))

find=False
result=0

for n in range(num,1,-1):
    if find:
        break
    for i in range(a-n+1): #0 1 2 (3) 0까지 (1번)
        for j in range(b-n+1): #0 1 2 3 4 (5) 2까지(3번)
            A=l[i][j]
            B=l[i][j+n-1]
            C=l[i+n-1][j]
            D=l[i+n-1][j+n-1]
            if A==B==C==D:
                result=n*n
                print(result)
                find=True

if result==0:
    print(1)





                

    
            
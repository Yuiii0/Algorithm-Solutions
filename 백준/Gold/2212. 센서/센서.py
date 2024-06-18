import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

censers=sorted(list(map(int,input().rstrip().split())))
result=[]

for i in range(n-1):
    result+=[censers[i+1]-censers[i]] # 각 센서간 차이
result.sort()
print(sum(result[:n-k])) 
    
import sys
input=sys.stdin.readline

n=int(input())
dist=list(map(int,input().rstrip().split()))
cost=list(map(int,input().rstrip().split()))


for i in range(2,len(cost)): #이전값과 비교해서 최소 비용으로 변경
    cost[i]=min(cost[i],cost[i-1]) #[5,2,2,1]

# 총 비용 계산
result=0
for i,d in enumerate(dist):
    result+=d*cost[i]

print(result)


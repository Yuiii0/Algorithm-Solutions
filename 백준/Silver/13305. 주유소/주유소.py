import sys
input=sys.stdin.readline

n=int(input())
dist=list(map(int,input().rstrip().split()))
cost=list(map(int,input().rstrip().split()))

minCost=cost[0]

for i in range(1,len(cost)): #이전값과 비교해서 최소 비용으로 변경
    minCost=min(minCost,cost[i])
    cost[i]=minCost #[5,2,4,1] 👉🏻[5,2,2,1]


# 총 비용 계산
result=0
for i,d in enumerate(dist):
    result+=d*cost[i]

print(result)


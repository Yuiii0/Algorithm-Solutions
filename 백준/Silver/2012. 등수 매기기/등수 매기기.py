from sys import stdin

input = stdin.readline
n=int(input())

expected_ranks=[int(input()) for _ in range(n)]
rank=set(range(1,n+1))
left_rank=[]
result=0
for r in expected_ranks:
    if r in rank:
        rank.remove(r)
    else:
        left_rank.append(r)

left_rank.sort()
result=0

for i,r in enumerate(rank):
    result+=abs(r-left_rank[i])

print(result)

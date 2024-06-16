from sys import stdin

input = stdin.readline
n=int(input())

# 학생이 적은 등수를 순회하며 우선 배치하고
# 배치 되지 못한 남은 등수 정렬-> 차이 최소화

expected_ranks=[int(input()) for _ in range(n)]
rank=set(range(1,n+1)) #1-n등
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

# 	85684	480
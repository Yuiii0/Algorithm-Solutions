import sys
from itertools import permutations

# k가 1이 될때까지 나누면서 몫이 l이상인지 확인
# 가장 작은 인수 저장

input = sys.stdin.readline
n = int(input().rstrip())
result=[]
for _ in range(n):
    d = int(input().rstrip())
    count=0
    for t in range(1,d):
        total_time=t+(t**2)
        if total_time<=d:
            count+=1
        else:
            break
    result.append(count)


for r in result:
    print(r)










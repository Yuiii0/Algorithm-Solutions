import sys
from itertools import permutations

# 가능한 3가지 모든 조합 생성 순서 (permutations)
# 1~12시가 아닌 H 제외

input=sys.stdin.readline
times=map(int,input().rstrip().split(':')) #시 분 초

result=0
for i,comb in enumerate(permutations(times,3)):
    if comb[0]>59 or comb[1]>59 or comb[2]>59 :
        break
    if 0<comb[0]<=12:
        result+=1


print(result)



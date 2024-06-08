# for c in comb: print(c)
#  실제로는 제너레이터 객체를 생성할 뿐이며, 출력할 때는 제너레이터 객체 전체가 출력됩니다.
# print("\n".join(str(c) for c in comb))

# 31120	40
import sys
from itertools import combinations
input=sys.stdin.readline

nine_heights = [int(input().strip()) for _ in range(9)]        

# 모든 조합을 찾고, 합이 100이 되는 경우 찾기


for comb in combinations(nine_heights,7):
    if sum(comb)==100:
        for c in sorted(comb):
            print(c)
        break
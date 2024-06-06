import sys
from functools import reduce

input = sys.stdin.readline

# 경우의 수
# 각 type별 값+1(착용x) 곱한후, 모두 착용하지 않는 경우-1

n = int(input())
# type별 카운트

for _ in range(n):
    dic = {}
    m = int(input())
    
    # If there are no clothes, print 0 and move to the next test case
    if m == 0:
        print(0)
        continue
    
    for _ in range(m):
        item, type = input().strip().split()
        dic[type] = dic.get(type, 0) + 1
    dic_values = list(dic.values())

    if len(dic_values) > 1:
        result = 1
        for v in dic_values:
            result *= v + 1
        print(result - 1)

    else:
        print(dic_values[0])

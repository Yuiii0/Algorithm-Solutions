#defaultDics 사용
#34008	132

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
fruits = defaultdict(int)
valid=True

for _ in range(n):
    fruit, num = input().strip().split()
    fruits[fruit] += int(num)
    
print('YES' if fruits[fruit] == 5 else 'NO')
        


# 이전 코드
# Counter 사용 = 120ms 34008	140
from collections import Counter

n=int(input())

fruits_counter=Counter()

for _ in range(n):
    fruit,num=input().split()
    fruits_counter[fruit]+=int(num)

print('YES' if 5 in fruits_counter.values() else 'NO')
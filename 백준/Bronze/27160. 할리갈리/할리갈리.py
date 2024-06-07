import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
fruits = defaultdict(int)
valid=True

for _ in range(n):
    fruit, num = input().strip().split()
    fruits[fruit] += int(num)
   

print('YES' if 5 in fruits.values() else 'NO')
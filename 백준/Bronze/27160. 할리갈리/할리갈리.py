from collections import Counter
import sys
input = sys.stdin.readline
n=int(input())

fruits_counter=Counter()

for _ in range(n):
    fruit,num=input().split()
    fruits_counter[fruit]+=int(num)

print('YES' if 5 in fruits_counter.values() else 'NO')
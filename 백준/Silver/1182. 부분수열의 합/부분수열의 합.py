import sys
from itertools import combinations
input = sys.stdin.readline

n,target = map(int,input().rstrip().split())
nums=list(map(int,input().rstrip().split()))
result=0
for i in range(1,n+1):
    for comb in combinations(nums,i):
        #print(sum(comb)) 
        if sum(comb)==target:
            result+=1

print(result)














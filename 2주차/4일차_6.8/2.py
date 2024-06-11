#31120	40


import sys
input=sys.stdin.readline
a,b=map(int,input().split())

nums=[]
for i in range(1,50): #N<1000
    for j in range(i):
        nums.append(i)

print(sum(nums[a-1:b]))
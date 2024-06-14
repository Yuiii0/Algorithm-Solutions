from sys import stdin

input = stdin.readline
n=int(input())
meetings=[list(map(int,input().split())) for _ in range(n)]

# 종료 시간 순
meetings.sort(key=lambda x: (x[1],x[0]))
p=0
count=1
for i in range(1,n):
    if meetings[p][1]<=meetings[i][0]:
        p=i
        count+=1
print(count)

import sys

n,k = map(int,sys.stdin.readline().split())

data =[]
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

prev = 0
for i in range(n):
    if data[prev][1:4] != data[i][1:4] :
        prev = i 
    if data[i][0] == k:
        print(prev+1)
        break
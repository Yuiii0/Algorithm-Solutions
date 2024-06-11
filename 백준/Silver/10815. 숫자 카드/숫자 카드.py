import sys
input=sys.stdin.readline

n=int(input())
sangs=set(map(int,input().rstrip().split()))


m=int(input())
num_set=list(map(int,input().rstrip().split()))


for s in num_set:
    # print(s)
    if s in sangs:
        print(1,end=' ')
    else:
        print(0,end=' ')

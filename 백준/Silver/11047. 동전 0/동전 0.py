import sys
input=sys.stdin.readline

n,money=map(int,input().rstrip().split())
units=[int(input()) for _ in range(n)]

units.sort(reverse=True) # 큰 화폐단위부터 나누기위해 내림차순 정렬

result=0
for unit in units:
    result+=money//unit
    money%=unit
print(result)
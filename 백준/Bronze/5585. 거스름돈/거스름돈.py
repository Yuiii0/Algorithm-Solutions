import sys
from heapq import *
input=sys.stdin.readline

unit=[500,100,50,10,5,1]
cost=int(input())
money=1000-cost # 거스름돈

count=0
for u in unit:
    count += money // u
    money %= u  # 큰 화폐 단위부터 거스름돈을 분배하고, 남은 금액
    if money==0:
        break

print(count)









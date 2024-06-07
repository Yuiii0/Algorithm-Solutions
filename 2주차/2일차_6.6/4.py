# 최소힙 37044	120

from heapq import *
import sys 

input=sys.stdin.readline

n=int(input())

heap=[]
for _ in range(n):
    num=int(input())
    #자연수=배열에 넣기
    if num:
        heappush(heap,num)
    #0=리턴후 삭제
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0) #힙이 비어있는 경우
import sys
from heapq import *

# 절대값이 작은값 - minHeap
# 부호를 표기해두었다가 출력할때 사용 (x,부호)
# 튜플 형식도 첫번째가 값이라면 minHeap 가능

input = sys.stdin.readline
n=int(input())

heap=[]
for _ in range(n):
    x=int(input())
    if x: # 추가
        t=(abs(x),-1 if x<0 else 1) #(x,부호)
        heappush(heap,t)
        #print('추가후',heap)
    else: # 출력/삭제
        if heap:
            temp=heappop(heap)
            print(temp[0]*temp[1])
        else:
            print(0) # 비어있다면 0 출력


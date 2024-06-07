#1차풀이
input = sys.stdin.readline
n=int(input())

heap=[]

num_list=[list(map(int,input().split())) for _ in range(n)]
print(num_list)
    
for num in num_list:
    for n in num:
        heapq.heappush(heap,(-n,n))


for i in range(n-1):
    heapq.heappop(heap)

print(heap[0][1])
# https://yuna0125.tistory.com/79

#2차 풀이

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int,input().split())) #[12,7,9,15,5]

    if not heap:
        for num in nums: 
            heapq.heappush(heap, num) # 초기값 n개 넣어주기 [5,7,9,12,15]
        
    else:
        for num in nums:
            if num > heap[0]:
                heapq.heappop(heap) # 맨앞제거하고
                heapq.heappush(heap, num) # 새로운 값 넣어주기
              
               
print(heap[0])

#33188	760
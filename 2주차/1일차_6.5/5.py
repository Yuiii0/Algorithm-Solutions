# 인쇄=맨앞요소 제거시, 
# list(stack)는 pop(0)=O(n)
# Queue는 popleft()=O(1)  -> Queue 사용

# 첫번째 요소가 queue에서 max값이여야 출력이 가능

import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
find=False


for _ in range(n):
    q=deque() #queue 생성 

    n,target=map(int,input().split())
    priority=list(map(int,input().split()))
    
    for idx,p in enumerate(priority):
        q.append((idx,p)) #(index:우선순위)
    
    result=0
    
    while True:
        # 첫번째 요소가 현재 큐에서 가장 큰 우선순위인지 확인
        max_priority=max(q,key=lambda x:x[1])[1]
        first=q.popleft()
  

        if first[1]==max_priority:
            result+=1
            #target 확인
            if target==first[0]:
              print(result)
              break
        else:
            #뒤로가기
            q.append(first)

# 34052	92
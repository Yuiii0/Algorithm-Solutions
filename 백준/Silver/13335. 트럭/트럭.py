import sys
from collections import deque
input = sys.stdin.readline

n,w,l=map(int,input().rstrip().split())
trucks=deque(list(map(int,input().rstrip().split())))
bridge=deque([0]*w) # 0으로 초기화해서 다리 생성

t=0

while trucks:
    truck=trucks[0]           #7
    # 다리 진입 전에, 다리 총 무게 계산
    bridge.popleft() # 맨 앞 트럭은 빠져나감
    if sum(bridge)+truck<=l:  #진입 가능
        bridge.append(trucks.popleft())  #다리 진입           
    else: # 하중초과
        bridge.append(0)

    t+=1

# 트럭이 모두 다리에 진입 후, 마지막 트럭까지 모두 건너는 시간=다리 길이만큼 소요
t+=w
print(t)







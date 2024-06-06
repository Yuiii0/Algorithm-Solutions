import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
notes=list(map(int,input().strip().split()))

#deck 생성 (풍선 번호,note)
deck=deque((i+1,note) for i,note in enumerate(notes))

result=[]

#처음은 1번 풍선
cur=0 #현재 포인터 idx

for _ in range(n):
    ballon,dx=deck.popleft() #풍선번호,이동값
    #p=deck[cur] #(1,3) 
    result.append(ballon) #result=[1,]

    #포인터 이동
    dx=p[1] #3이동해라라
    nx=cur+dx #포인터 이동할 거리
    print('nx',nx)

    #index range
    if nx>len(deck):
        print('오른쪽 초과')
        nx=nx%len(deck)
        print(len(deck),nx)
    result.append(deck[nx][0]) 
    print(nx,'nx')
    print('쪽지 까봄',deck[nx][1])


     

    #1 4 5 3 2    
    #풍선 없애기
    deck.remove(p)
    # 삭제될 수<새로운 cur의 값 -1
    # 삭제될 수>새로운 cur의 값 cur 그대로

    if len(deck)>2 and p[0]<deck[nx][0]:
        cur=nx-1
    else:
        cur=nx
    if cur<0:
        cur=len(deck)+cur
        
    print('풍선 업데이트',deck)
    # 이동하고 새로운 cur 업데이트 3

    print(result) 
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deck=deque()
for i in range(n):
    cmd_list=input().split()
    cmd=cmd_list[0]

    if cmd=='push_front':
        x=cmd_list[1]
        deck.appendleft(int(x))
    elif cmd=='push_back':
        x=cmd_list[1]
        deck.append(int(x))
    elif cmd=='pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif cmd=='pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)  
    elif cmd=='size':
        print(len(deck))
    elif cmd=='empty':
        if deck:
            print(0)
        else:
            print(1)
    elif cmd=='front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    else:
        if deck:
            print(deck[-1])
        else:
            print(-1)
        

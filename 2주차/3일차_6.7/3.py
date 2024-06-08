import sys

input = sys.stdin.readline

N = int(input())
first_tickets = sorted(map(int, input().split()))  
isEnd=True

for i in range(N): #0 1 2 3 4
    if i+1!=first_tickets[i]:
        print(i+1)
        isEnd=False
        break

#1차에서 다팔린 경우
if isEnd:
    print(N+1)
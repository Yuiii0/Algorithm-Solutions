import sys
from itertools import permutations
input = sys.stdin.readline

n=int(input())
k=int(input())


cards=[int(input()) for _ in range(n)]


selected_cards=set()
for p in permutations(cards,k):
    selected_cards.add(''.join(map(str,p)))  #(2, 1, 13)=(21, 1, 3) 같은경우이므로, 문자열로 변환후 set에 넣어줌
print(len(selected_cards))

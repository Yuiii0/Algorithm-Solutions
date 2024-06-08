import sys
from itertools import combinations
input=sys.stdin.readline

nine_heights=[int(input())for _ in range(9)]        
nine_heights.sort()

temp=nine_heights[:7]
large=nine_heights[-2:]
t=100-sum(temp)


out_idx=0
in_value=0
# 빠지고 새로 들어올 수의 합=t가 되는 조합 찾기
for i in large: # 23 25
    for j,out in enumerate(temp):
        if t==(i-out):
            out_idx=j
            in_value=i
            break
            

temp.pop(out_idx)
temp.append(in_value)

for t in temp:
    print(t)







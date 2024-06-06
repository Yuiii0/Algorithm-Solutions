# 그릇을 순회하면서 이전그릇 방향에 따라 분기
# 같은방향+5, 다른방향+10

import sys
input=sys.stdin.readline
bowls=input().rstrip()

result=10

for i in range(1,len(bowls)):
    #이전 그릇과 방향 비교 
    result+=5 if bowls[i-1]==bowls[i] else 10

print(result)
    

#31120	44
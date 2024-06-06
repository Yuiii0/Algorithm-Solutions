# row 순회하면서 max값을 찾고, 최대값과 비교한 후 업데이트
# 최대값 위치 저장

import sys
input=sys.stdin.readline

max_value=0
max_position=[0,0] 

for row in range(9):
    x_list=list(map(int,input().split()))
    if max(x_list)>max_value:
        max_value=max(x_list)

        max_position[0]=row 
        max_position[1]=x_list.index(max(x_list)) 


print(max_value)
print(max_position[0]+1,max_position[1]+1)

        
# 31120 40        
import sys
input=sys.stdin.readline

max_value=0
max_position=[0,0] #row
for row in range(9):
    x_list=list(map(int,input().split()))
    if max(x_list)>max_value:
        max_value=max(x_list)
        #print(max(x_list))
        max_position[0]=row 
        max_position[1]=x_list.index(max(x_list)) 


print(max_value)
print(f'{max_position[0]+1} {max_position[1]+1}')

        
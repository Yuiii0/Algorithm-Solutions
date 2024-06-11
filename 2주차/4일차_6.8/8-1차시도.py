import sys
input=sys.stdin.readline
# 최대값을 기준으로 y값은 왼편은 오름차순, 오른편은 내림차순만 가능

# 스택이용
# stack의 top과 비교해서 큰수일때만 담기 
# left: 왼쪽부터 순회 (for 증가 패턴)
# right: 오른쪽부터 순회 (for 감소 패턴)

n=int(input())

num_list=[]
for _ in range(n):
    n,m=map(int,input().rstrip().split())
    num_list.append((n,m)) #(x,y) 리스트
# 정렬 (x기준)
num_list.sort()

# top 최대값 찾기 
top=max(num_list,key=lambda x:x[1])
top_idx=num_list.index(top) #3
top_y=top[1]
top_x=top[0] #8
min_x=num_list[0][0]
max_x=num_list[len(num_list)-1][0]
# print(min_x,max_y)

# left (top_x 기준)

left_stack=[]
result=0

for num in num_list[:top_idx]:
    y=num[1]
    print(y)
    if left_stack:
        if y>left_stack[-1][1]:
            print(left_stack[-1])
            left_stack.append(num)
            
    else:
        left_stack.append(num)

    print('left_stack',left_stack)

 # [2, 3, 4, 5, 6, 7]
for i in range(len(left_stack)-1):
    # 현재 x
    print(left_stack[i][0])
    # 다음 x
    print(left_stack[i+1][0])
    gap=left_stack[i+1][0]-left_stack[i][0]
    print('gap',gap)
    result+=left_stack[i][1]*gap
print(result)
result+=
    
# left_list=[i for i in range()]


#right
# right_list=[i for i in range(top_x+1,max_x+1)] #[9, 10, 11, 12, 13, 14, 15]


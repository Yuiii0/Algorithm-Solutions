import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    temp = list(input().strip())  
    flag = True  

    for bracket in temp:
        # open 괄호는 저장
        if bracket == '(':
            stack.append(bracket)
        # close 괄호라면 stack에서 짝을 이루는 괄호 꺼내기
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                flag = False  
                break

    if flag:  
        if stack:
            print('NO')
        else:
            print('YES')

# 31120	44
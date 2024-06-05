import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    temp = list(input().strip())  # .strip()을 사용하여 입력의 양 끝 공백을 제거
    valid = True  # 유효성을 체크하는 변수 추가

    for bracket in temp:
        # 여는 괄호는 저장
        if bracket == '(':
            stack.append(bracket)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                valid = False  # 잘못된 경우 valid를 False로 설정
                break

    if valid:  # 루프가 정상적으로 종료된 경우에만 stack을 체크
        if stack:
            print('NO')
        else:
            print('YES')
  
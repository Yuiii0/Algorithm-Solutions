from collections import deque


def is_valid_parentheses(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in brackets.values():  # 여는 괄호는 스택에 넣기
            stack.append(char)
        elif char in brackets.keys():  # 닫는 괄호가 나왔을 때
            # 스택이 비어있거나 스택의 top이 현재 닫는 괄호에 대응하는 여는 괄호가 아니면 False
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0


def solution(s):
    answer = 0
    queue = deque(s)

    for _ in range(len(s)):
        # 올바른 괄호 여부 체크
        if is_valid_parentheses(''.join(queue)):
            answer += 1

        # 문자열 회전
        queue.append(queue.popleft())

    return answer



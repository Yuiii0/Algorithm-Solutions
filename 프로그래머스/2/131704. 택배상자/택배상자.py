def solution(order):
    answer = 0
    sub_container = [] # stack
    current = 1 

    for o in order:
        # 현재 순서의 상자가 나올 때까지 보조 컨테이너에 쌓기
        while current <= o:
            sub_container.append(current)
            current += 1

        # 보조 컨테이너의 가장 위의 상자가 순서에 맞는 경우 트럭에 싣기
        if sub_container and sub_container[-1] == o:
            sub_container.pop()
            answer += 1
        else:
            break

    return answer


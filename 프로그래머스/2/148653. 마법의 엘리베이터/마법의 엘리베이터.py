def solution(storey):
    answer = 0

    while storey > 0:
        last_digit = storey % 10  # 현재 층수의 마지막 자리 수
        if last_digit > 5:
            # 현재 자릿값이 6~9일 경우, 10으로 올림
            answer += (10 - last_digit)  # + 버튼 클릭 수
            storey += (10 - last_digit)   # 층수 올림
        elif last_digit < 5:
            # 현재 자릿값이 0~4일 경우, 0으로 내림
            answer += last_digit  # - 버튼 클릭 수
        else:  # last_digit == 5
            # 현재 자릿값이 5일 경우
            next_digit = (storey // 10) % 10  # 다음 자릿값 확인
            if next_digit >= 5:
                # 다음 자릿값이 5 이상일 경우, 10으로 올림
                answer += 5  # 클릭 수 5
                storey += 5  # 층수 올림
            else:
                # 다음 자릿값이 0~4일 경우, 0으로 내림
                answer += 5  # 클릭 수 5
                storey -= 5  # 층수 내림

        storey //= 10  # 다음 자릿수로 이동

    return answer

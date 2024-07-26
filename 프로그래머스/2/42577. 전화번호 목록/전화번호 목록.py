def solution(phone_book):
    phone_map = {}

    for number in phone_book:
        phone_map[number]=True

    for number in phone_book:
        for i in range(1,len(number)):
            prefix=number[:i] # 가능한 모든 후보 접두어 생성
            if prefix in phone_map:
                return False

    return True
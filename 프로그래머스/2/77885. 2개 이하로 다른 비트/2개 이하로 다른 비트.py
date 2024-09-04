# 짝수: 마지막 비트가 0이기 때문에, 마지막 비트를 1로 바꿔주는 것이 답 -> 숫자+1
# 홀수: 가장 뒤에 있는 0을 1로 바꾸고, 그 다음 비트를 1에서 0으로 바꿔준다.
def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
            continue

        bin_number='0'+bin(number)[2:]
        last_zero_idx=bin_number.rfind('0')
        bin_number=bin_number[:last_zero_idx]+'10'+bin_number[last_zero_idx+2:]
        answer.append(int(bin_number,2))

    return answer


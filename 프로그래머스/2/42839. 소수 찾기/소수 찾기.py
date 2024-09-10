from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums=set()

    # 가능한 숫자 카드 조합 만들기
    for i in range(1,len(numbers)+1):
        for perm in permutations(numbers, i):
            nums.add(int(''.join(perm)))

    # 소수 판별
    for num in nums:
        if is_prime(num):
            answer+=1

    return answer


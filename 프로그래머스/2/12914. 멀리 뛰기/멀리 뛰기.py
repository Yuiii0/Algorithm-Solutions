def factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def combination(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def solution(n):
    MOD = 1234567
    count = 0

    # 2칸의 개수를 i로 두고, 최대 2칸의 개수는 n//2
    for i in range(n // 2 + 1):
        # 1칸의 개수는 n - 2 * i
        num_ones = n - 2 * i
        # 전체의 경우의 수 계산
        count += combination(num_ones + i, i)  # (num_ones + i)C(i)

    return count % MOD


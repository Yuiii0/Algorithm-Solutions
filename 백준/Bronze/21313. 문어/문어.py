import sys
input = sys.stdin.readline

n = int(input())
result = [1, 2] * (n // 2)
if n % 2 == 1:
    result.append(3)
print(*result)

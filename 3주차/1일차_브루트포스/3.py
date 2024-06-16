
import sys

# 소수
# l보다 작은 값으로 나눠지면, bad

input = sys.stdin.readline
k, l = map(int, input().rstrip().split())


for divisor in range(2,l):
    if k%divisor==0:
        print('BAD',divisor)
        break
else:
    print('GOOD')



# 31120	280







# 공백 0 1 2 3 4
# *   5 4 3 2 1

n=int(input())
for i in range(n):
    # 공백 i + 별 n-i
    print(' '*i+'*'*(n-i))
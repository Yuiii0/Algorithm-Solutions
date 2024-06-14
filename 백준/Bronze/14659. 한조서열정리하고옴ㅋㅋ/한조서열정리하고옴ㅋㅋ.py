import sys
input = sys.stdin.readline

n = int(input())
peaks = list(map(int, input().rstrip().split()))

best_man = peaks[0]
count_list = []
count = 0

for i in range(1, n):
    if best_man > peaks[i]:
        count += 1
    else:
        count_list.append(count)
        count = 0
        best_man = peaks[i]

# 마지막 count도 추가해야 합니다.
count_list.append(count)

print(max(count_list))

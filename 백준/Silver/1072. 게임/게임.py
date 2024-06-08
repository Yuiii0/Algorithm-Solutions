import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().strip().split())

# 현재 승률 계산
z = m * 100 // n

# 승률이 100%이면 더 이상 변화하지 않음
if z >= 99:
    print(-1)
else:
    # 이분 탐색 초기 범위 설정
    start = 1
    end = 1000000000  # 충분히 큰 숫자로 설정

    # 이분 탐색
    result = -1
    while start <= end:
        mid = (start + end) // 2
        new_z = (m + mid) * 100 // (n + mid)
        if new_z > z:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)

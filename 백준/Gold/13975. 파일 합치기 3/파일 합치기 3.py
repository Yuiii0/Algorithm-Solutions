import sys
import heapq

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    nums = list(map(int, input().strip().split()))
    heapq.heapify(nums)  # 리스트를 최소 힙으로 변환

    result = 0
    while len(nums) > 1:
        # 두 개의 최솟값 추출
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)

        # 두 값을 더한 후 결과에 추가
        temp = first + second
        result += temp

        # 합한 값을 힙에 다시 삽입
        heapq.heappush(nums, temp)

    print(result)

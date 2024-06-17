import sys
from collections import deque

input = sys.stdin.readline

# 사진틀의 개수
n = int(input())
# 전체 추천 횟수
m = int(input())
# 추천 받은 학생 리스트
num_list = list(map(int, input().strip().split()))

# 사진틀을 위한 deque
queue = deque()
# 학생별 추천수 저장 dict
recommendations = {}

for num in num_list:
    if num in recommendations:
        recommendations[num] += 1
    else:
        if len(queue) >= n:
            # 추천수가 가장 적은 학생 찾기
            min_recommend = float('inf')
            for candidate in queue:
                if recommendations[candidate] < min_recommend:
                    min_recommend = recommendations[candidate]
            
            # 가장 적은 추천수를 가진 후보 중 가장 오래된 후보 찾기
            for candidate in queue:
                if recommendations[candidate] == min_recommend:
                    queue.remove(candidate)
                    del recommendations[candidate]
                    break
        
        # 새로운 학생 추가
        recommendations[num] = 1
        queue.append(num)

# 최종 후보 번호만 추출하여 오름차순 정렬
result = sorted(queue)
print(*result)

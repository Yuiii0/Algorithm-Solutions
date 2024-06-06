import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))


# 2번과 3번 중 어느것을 결정할지-> 중간 인덱스를 기준으로 해당index가 가까운곳으로
# 큐생성
q = deque([i for i in range(1, n + 1)])


result = 0
for num in num_list:

    while True:
        # 맨앞요소가 빠져나갈수있는지 확인
        if q[0] == num:
            q.popleft()
            break

        idx = q.index(num)
        mid = len(q) // 2
        if idx <= mid:
            # 2번
            q.append(q.popleft())
        else:
            q.appendleft(q.pop())
        result += 1

print(result)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, target):
    queue = deque([start])
    visited[start] = 0  # 시작위치=0

    while queue:
        cur = queue.popleft()

        if cur == target:
            return visited[cur]  # 이동 시간(s)

        for i in range(3):
            if i < 2:  # 앞으로 또는 뒤로 이동
                nx = cur + dx[i]
            else:  # 텔레포트 이동
                nx = cur * dx[i]

            # 경계 체크 및 방문 여부 확인
            if 0 <= nx <= max(n, m) * 2 and visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                queue.append(nx)

n, m = map(int, input().rstrip().split())
visited = [-1] * (max(n, m) * 2 + 1)  
cur = n  # 수빈 현재 위치
dx = [1, -1, 2]  # 수빈의 이동 방식

# 시작 위치가 목표 위치와 같은 경우
if n == m:
    print(0)
else:
    result = bfs(cur, m)
    print(result)

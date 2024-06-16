import sys

input = sys.stdin.readline

n = int(input()) 

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    commands = input().strip() 

   
    direction = 0  # 초기방향=북쪽 (0: 북, 1: 동, 2: 남, 3: 서)
    x, y = 0, 0  # 초기위치
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0

    for command in commands:
        if command == 'F':
            x += dx[direction]   # 현재 방향에서 dx,dy만큼 이동
            y += dy[direction]
        elif command == 'B':
            x -= dx[direction]
            y -= dy[direction]   # 현재 방향의 반대로 dx,dy만큼 이동
        elif command == 'L':
            direction = (direction - 1) % 4    # 방향 업데이트
        elif command == 'R':
            direction = (direction + 1) % 4

        # 좌표 이동 후 최소,최대값 업데이트
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # 직사각형 넓이 계산
    result = (max_x - min_x) * (max_y - min_y)
    print(result)

import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
move= [[1,0],[1,1],[0,1],[-1,1]]
N = 19
result = 0

for i in range(N):
    for j in range(N):
        if board[i][j] != 0: # 돌이 있는 칸이면
            stone = board[i][j] # 돌의 색 저장
            for dy, dx in move: 
                ny, nx, cnt = i + dy, j + dx, 1
                while 0 <= ny < N and 0 <= nx < N and board[ny][nx] == stone: # 범위내에 있고, 해당 방향에 돌 색이 있다면
                    cnt += 1 # 1개씩 증가
                    if cnt == 5: # 육목 확인
                        # 반대 방향 확인 : 시작점(i,j)기준으로 
                        if 0 <= i - dy < N and 0 <= j - dx < N and board[i-dy][j-dx] == stone: # 반대칸에 하나 더 있거나
                            break
                        # 순회 방향 확인
                        if 0 <= ny + dy < N and 0 <= nx + dx < N and board[ny+dy][nx+dx] == stone: 
                            break
                        result=stone
                        y, x = i+1, j+1
                    ny += dy # 이동
                    nx += dx 
if result > 0:
    print(result)
    print(y,x)
else:
    print(0)

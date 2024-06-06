import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 보드 읽기
board = []
for _ in range(n):
    board.append(input().rstrip())

result = []

# 가능한 보드 순회
for i in range(n - 7): 
    for j in range(m - 7): 
        w_board = 0
        b_board = 0
        #8x8로 자르기
        for y in range(i, i + 8):
            for x in range(j, j + 8):
                temp=board[y][x]
                if (x + y) % 2 == 0:
                    if temp != 'W':
                        w_board += 1
                    if temp != 'B':
                        b_board += 1
                else:
                    if temp != 'B':
                        w_board += 1
                    if temp != 'W':
                        b_board += 1
        result.append(min(w_board, b_board))

print(min(result))

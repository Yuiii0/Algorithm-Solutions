import sys

input = sys.stdin.readline

king, stone, n = input().rstrip().split()

# 이동 방향 (row,col)
move = {
    'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
    'RT': (-1, 1), 'RB': (1, 1), 'LT': (-1, -1), 'LB': (1, -1)
}
cols = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
reversed_cols = {v: k for k, v in cols.items()}

# 초기 위치 세팅
king_cx, king_cy = cols[list(king)[0]], 8 - int(list(king)[1])
stone_cx, stone_cy = cols[list(stone)[0]], 8 - int(list(stone)[1])

# 돌을 이동시킬수 없다면 king도 이동시킬 수 없다.

for _ in range(int(n)):
    direction = move[input().rstrip()]
    dy, dx = direction[0], direction[1]
    # print('이동 전', king_cy, king_cx)
    king_nx, king_ny = king_cx + dx, king_cy + dy

    
    if 0 <= king_nx < 8 and 0 <= king_ny < 8:
        # king과 돌의 충돌여부 확인
        if king_ny == stone_cy and king_nx == stone_cx:  # stone=king 충돌
            stone_ny = stone_cy + dy
            stone_nx = stone_cx + dx
            if 0 <= stone_nx < 8 and 0 <= stone_ny < 8:  # 돌 이동가능
                # stone 이동
                stone_cy = stone_ny
                stone_cx = stone_nx
                
            else:  # 돌 이동 불가
                continue
        # king 이동
        king_cx = king_nx
        king_cy = king_ny

print(reversed_cols[king_cx] + str(8 - king_cy)) 
print(reversed_cols[stone_cx] + str(8 - stone_cy))



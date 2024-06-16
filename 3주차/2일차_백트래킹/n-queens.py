def is_safe(board, row, col):
    # 현재 위치 (row, col)에 퀸을 놓는 것이 안전한지 확인하는 함수
    for i in range(row):
        # 같은 열에 다른 퀸이 있는지 확인  # 좌상향 대각선에 다른 퀸이 있는지 확인 # 우상향 대각선에 다른 퀸이 있는지 확인
        # board[i]=col, i=row
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row):
    n = len(board)
    # 모든 행에 퀸을 성공적으로 배치한 경우
    if row == n:
        return True
    # 현재 행에 대해 모든 열을 시도
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # 퀸을 (row, col)에 배치
            if solve_n_queens(board, row + 1):  # 다음 행으로 이동하여 재귀적으로 해결 시도
                return True
            # 백트래킹: 퀸을 제거하고 다음 열을 시도
    return False

def print_board(board):
    n = len(board)
    # 보드를 출력하는 함수
    for row in range(n):
        line = ['.'] * n  # 모든 칸을 '.'으로 초기화
        line[board[row]] = 'Q'  # 퀸이 있는 칸을 'Q'로 설정
        print(' '.join(line))  # 보드의 한 행을 출력

n = 8  # N-Queens 문제의 N 값
board = [-1] * n  # 보드를 초기화 (-1은 퀸이 배치되지 않음을 의미)
if solve_n_queens(board, 0):
    print_board(board)  # 해결된 보드를 출력
else:
    print("No solution found")  # 해결책이 없는 경우 메시지 출력

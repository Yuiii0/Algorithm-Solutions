import sys
input = sys.stdin.readline

def find_area(pillars):
    pillars.sort()
    
    # 가장 높은 기둥 찾기
    max_pillar = max(pillars, key=lambda x: x[1])
    max_index = pillars.index(max_pillar)
    
    # 왼쪽 부분 계산
    left_max_height = 0
    left_area = 0
    for i in range(max_index + 1):
        if pillars[i][1] > left_max_height:
            left_max_height = pillars[i][1]
        if i < max_index:
            left_area += left_max_height * (pillars[i + 1][0] - pillars[i][0])
    
    # 오른쪽 부분 계산
    right_max_height = 0
    right_area = 0
    for i in range(len(pillars) - 1, max_index - 1, -1):
        if pillars[i][1] > right_max_height:
            right_max_height = pillars[i][1]
        if i > max_index:
            right_area += right_max_height * (pillars[i][0] - pillars[i - 1][0])
    
    # 전체 면적 계산
    total_area = left_area + right_area + max_pillar[1]
    
    return total_area

# 입력 처리
n = int(input().strip())
pillars = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 결과 계산 및 출력
result = find_area(pillars)
print(result)

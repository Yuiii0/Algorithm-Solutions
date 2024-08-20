# 가장 큰 수는 필수로 가져가야하는 수
# 가로,세로 중 더 큰 쪽을 가장 큰 수와 같은 방향으로 돌리기
# -> [a,b] 더 큰수를 a로 정렬해줌
# 각 가로, 세로 중 가장 큰 값을 뽑아 너비를 구함


def solution(sizes):
    max_width=0
    max_height=0
    for size in sizes: # [[60, 50], [70, 30], [60, 30], [80, 40]]
        size.sort(reverse=True)
        max_width=max(max_width,size[0])
        max_height =max(max_height,size[1])



    return max_width*max_height
# 테두리 1줄 -> brown =


def solution(brown, yellow):
    total=brown+yellow

    for n in range(3,total):
        if total%n==0:
            height=n
            width=total//n
            # total로 만들수 있는 가로,세로
            # brown이 테두리 1줄이 만들어지는 지 확인
            if brown==2*width+2*height-4:
                return [width,height]


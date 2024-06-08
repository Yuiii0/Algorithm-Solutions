import sys

def sol(datas):
    count = 0
    while True:
        max_value = max(datas)
        if max_value == datas[0]:  # 1번이 최다득표가 되면 (동점 경우 포함)
            if datas.count(max_value)==1:
                return count
            else:
                return count+1

        else:
            max_idx = datas.index(max_value)  # 최다 득표 후보의 인덱스 찾기
            datas[max_idx] -= 1  # 최다 득표 후보의 득표수 1 감소
            datas[0] += 1  # 1번 후보에게 득표return count 추가
            count += 1


def read_input():
    input = sys.stdin.readline
    n = int(input().strip())
    input_list = [int(input().strip()) for _ in range(n)]  # 득표수 리스트
    return input_list

def main():
    datas = read_input()
    result = sol(datas)
    print(result)

if __name__ == "__main__":
    main()

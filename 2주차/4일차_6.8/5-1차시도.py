import sys


def find_max_bridge_count(num):
    if num<=3:
        return 1
    else:
        i=1 #1부터 시작해서 1씩 증가
        cur=1 #처음 시작
        while True:
            cur+=i # 7+=4 11
            if cur+i+1>num:
                return i
            i += 1


def read_input():
    input = sys.stdin.readline
    n=int(input())
    input_list=[int(input()) for _ in range(n)]

    return input_list

def main():
    datas=read_input()
    for data in datas:
        result = find_max_bridge_count(data)
        print(result)


# 1s
# 시간초과




if __name__ == "__main__":
    main()
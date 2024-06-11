import sys

def find_max_bridge_count(target):
    if target <= 3:
        return 1
    i = 0
    num = 1
    while num <= target:
        i += 1
        num += i
    return i-1




def make_bride_list(target):
    i = 1
    num = 1
    while num < target:
        num += i
        i += 1
    return num

def read_input():
    input = sys.stdin.readline
    n = int(input().strip())
    input_list = [int(input().strip()) for _ in range(n)]
    return input_list

def main():
    datas = read_input()
    for data in datas:
        result = find_max_bridge_count(data)
        print(result)

if __name__ == "__main__":
    main()

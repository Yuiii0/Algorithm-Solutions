#31120	48

import sys

def binary_search(n,m,z):
    if z >= 99:
        return -1

    start = 1
    end = n

    result = 0
    while start <= end:
        mid = (start + end) // 2
        new_z = (m + mid) * 100 // (n + mid)
        if z + 1 <= new_z:  # 오른쪽 탐색
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


def read_input():
    input = sys.stdin.readline
    n,m=map(int,input().strip().split())
    z = m * 100 // n  # 현재 승률
    return n,m,z

def main():
    n,m,z = read_input()
    result = binary_search(n,m,z)
    print(result)

if __name__ == "__main__":
    main()

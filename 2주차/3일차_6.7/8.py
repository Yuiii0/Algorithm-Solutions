#	125620	612

import sys
input=sys.stdin.readline

n=int(input())
sangs=set(map(int,input().rstrip().split()))


m=int(input())
num_set=list(map(int,input().rstrip().split()))


for s in num_set:
    # print(s)
    if s in sangs:
        print(1,end=' ')
    else:
        print(0,end=' ')



# binary search
import sys
input = sys.stdin.readline

n = int(input())
sangs = list(map(int, input().rstrip().split()))

m = int(input())
num_list = list(map(int, input().rstrip().split()))

# 이분 탐색을 위한 정렬
# 113328	1868
sangs.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return False

for target in num_list:
    if binary_search(sangs, target):
        print(1, end=' ')
    else:
        print(0, end=' ')

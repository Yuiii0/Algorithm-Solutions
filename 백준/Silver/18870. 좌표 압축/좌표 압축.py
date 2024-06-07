import sys
input = sys.stdin.readline


n=int(input())

# 오름차순으로 정렬해 idx 값을 저장 
# 순회하면서 key값으로 idx 찾기

#dict {0: -10, 1: -9, 2: 2, 3: 4, 4: 4}
num_list=list(map(int,input().split()))
num_set=set(num_list)

dict={}
for i,num in enumerate(sorted(list(num_set))):
    if not num in dict:
        dict[num]=i

for num in num_list:
    print(dict[num],end=' ')
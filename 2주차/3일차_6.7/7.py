import sys
input = sys.stdin.readline


n=int(input())

# 오름차순으로 몇번째인지 idx 값을 저장 (중복=set) 
# 순회하면서 key값으로 idx 찾기

num_list=list(map(int,input().split()))
num_set=set(num_list)

dict={}
for i,num in enumerate(sorted(list(num_set))):
    if not num in dict:
        dict[num]=i

for num in num_list:
    print(dict[num],end=' ')
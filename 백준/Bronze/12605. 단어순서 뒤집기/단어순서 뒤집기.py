# 단어들 리스트 생성하고
# 뒤에서부터 순회하면서 stack에 append

import sys
input=sys.stdin.readline
n=int(input())

for i in range(n):
    words=input().split()
    print(f'Case #{i+1}:',end=' ')
    for word in words[::-1]:
        print(word, end=' ')
    print()

import sys 
input=sys.stdin.readline

n=int(input())

pw_list=[]
for i in range(n):
    pw_list.append(input().strip())

# 순회하면서 뒤집어진 문자열이 있는지 확인
for pw in pw_list:
    pw_reversed=pw[::-1]
    if pw_reversed in pw_list:
        print(len(pw),pw[len(pw)//2])
        break

 #31120	36       
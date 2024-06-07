import sys
input=sys.stdin.readline

N=int(input())

univ_list=[] # [university,num]
for _ in range(N):    
    M=int(input())
    univ_list=[input().split() for _ in range(M)]
    print(sorted(univ_list,key=lambda x:-int(x[1]))[0][0])
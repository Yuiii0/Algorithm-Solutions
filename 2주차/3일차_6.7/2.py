import sys
input=sys.stdin.readline

N=int(input())

univ_list=[] # [university,num]
for _ in range(N):    
    M=int(input())
    univ_list=[input().split() for _ in range(M)]
    # num 오름차순으로 정렬
    print(sorted(univ_list,key=lambda x:-int(x[1]))[0][0])

#31120	40




# 함수로 왜 트렬ㅆ는지 확인하기
import sys
input=sys.stdin.readline


    
def read_input(N):
    univ_list=[] # [university,num]
    for _ in range(N):  
        M=int(input())
        univ_list=[input().split() for _ in range(M)]
    return univ_list
             

def main():
    N=int(input())
    # num 오름차순으로 정렬
    univ_list=read_input(N)
    print(sorted(univ_list,key=lambda x:-int(x[1]))[0][0])


if __name__=="__main__":
    main()
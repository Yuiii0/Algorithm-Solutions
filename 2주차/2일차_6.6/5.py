import sys
input = sys.stdin.readline

n=int(input())
r=31
M=1234567891
#알파벳:정수 hash 생성
input_hash={chr(ord('a')+i) :i+1 for i in range(26)}            

s=input()
result=0

for i in range(n):
    # 1.정수 치환
    str_to_num=input_hash[s[i]]
    # 2. sum
    result+=str_to_num*(r**i)

# mod
print(result%M)
    
 
#31120	44       

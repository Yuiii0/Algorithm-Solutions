

import sys
n,b=sys.stdin.readline().split()

# 문자열(A-Z) 숫자로 치환
# 아스키코드 A=65 to Z=90 이용 (ord)
result=0


for i in range(len(n)):
    num=n[i]
    if num.isdigit():
        num= int(n[i])
    else:
        num=ord(n[i])-55
    result+=int(b)**i*num

print(result)
#왜 오류나는지 잘 모르겠음-> 아 거꾸로 돌아야함 

################################

import sys
n,b=sys.stdin.readline().split()

nums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result=0

for i,num in enumerate(n[::-1]):
    result+=int(b)**i*nums.index(num)

print(result)

#31120	36
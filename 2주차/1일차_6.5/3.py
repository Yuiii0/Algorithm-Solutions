# 입력으로 받은 문자열-> 숫자로 변환
# 숫자가 소수인지 판별

import sys
import math
input=sys.stdin.readline

words=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

input_word=input().strip()

#소수 판별 함수
def is_prime(n):
    if n<=3:
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True


#숫자로 변환
num_word=0
for s in input_word:
    num_word+=words.index(s)+1


#소수단어 판별
if is_prime(num_word):
    print('It is a prime word.')
else:
    print('It is not a prime word.')

    
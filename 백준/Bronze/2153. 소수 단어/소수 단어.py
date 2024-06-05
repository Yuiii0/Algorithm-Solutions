# 입력으로 받은 문자열-> 숫자로 변환
# 숫자가 소수인지 판별

import sys
import math
input=sys.stdin.readline

words = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30,
    'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
    'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40,
    'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
    'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
    'Y': 51, 'Z': 52
}

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
num_word=sum(words.get(s,0) for s in input_word)
# for s in input_word:
#     num_word+=
#print(num_word)


#소수단어 판별
if is_prime(num_word):
    print('It is a prime word.')
else:
    print('It is not a prime word.')

    
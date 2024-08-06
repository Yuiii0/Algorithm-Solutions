from itertools import  product


def solution(word):
    word_list=[]
    vowel = ['A', 'E', 'I', 'O', 'U']

    for i in range(1,6):
        for per in product(vowel, repeat=i):
            word_list.append(''.join(per))

    word_list.sort()
    return word_list.index(word)+1
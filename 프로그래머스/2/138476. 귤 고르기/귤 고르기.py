# 종류 최소화를 위해 카운트를 해서 가장 개수가 많은 종류부터 담기

from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter=Counter(tangerine)
    sorted_tangerine = counter.most_common()


    for tangerine in sorted_tangerine:
        if k<=0:
            return answer
        k-=tangerine[1]
        answer+=1


    return answer
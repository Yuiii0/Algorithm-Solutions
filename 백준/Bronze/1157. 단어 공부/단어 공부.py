from collections import Counter

#대문자로 치환 후 문자별 카운트
#value가 같다면 -> ?출력
#빈도수 가장 큰 문자 대문자로 출력

word=input().upper()
word_counter=Counter(word)

#빈도수가 가장 큰 value를 찾아서 1도 같은지판단

#오름차순으로 정렬
value_list = sorted(word_counter.items(), key=lambda x:x[1],reverse=True)

#max값이 유일한지 확인
if len(value_list)==1:
    print(value_list[0][0])

else:
    if value_list[0][1]==value_list[1][1]:
        print('?')
    else:
        print(value_list[0][0])






#대문자로 치환 후 문자별 카운트
#최빈값이 유일하지 않다면 -> ?출력
#빈도수 가장 큰 문자 대문자로 출력

word=input().upper()
word_list = list(set(word)) 
count_list=[]

#문자 순회하면서 카운트
for i in word_list:
    count=word.count(i) #word에 해당 문자열이 몇개있는지
    count_list.append(count)


#max count값이 유일하지 않으면 ? 출력
if count_list.count(max(count_list))>1:
    print('?')

#최반값 index찾아서, word_list[index]출력
else: 
    print(word_list[count_list.index(max(count_list))])

import sys
input=sys.stdin.readline

length=[]
words=[]
#input 리스트 생성
for _ in range(5):
    word=list(input().strip())
    words.append(word)
    length.append(len(word))

result=''
#row 순회하면서, 각 i번째 글자 result에 추가
for i in range(max(length)):
    for j in range(5):
        if i<length[j]: #각 단어 길이가 다르기 때문
             result+=words[j][i]

print(result)

#31120	44
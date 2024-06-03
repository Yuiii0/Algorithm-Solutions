import sys
input=sys.stdin.readline

#배열 만들고나서, 인덱스 할당에서 돌리고 합치기
# x랑 y돌면서 조합해서 넣기


length=[]
words=[]

for _ in range(5):
    word=list(input().strip())
    words.append(word)
    length.append(len(word))

result=''
for i in range(max(length)):
    for j in range(5):
        if i<length[j]:
             result+=words[j][i]

print(result)
        

    

        
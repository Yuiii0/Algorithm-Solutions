# prev_last=cur_first
# 중복x -> set이용
# A의 단어리스트 후보에서 ? 찾기

import sys
n = int(sys.stdin.readline())
lines=sys.stdin.read().splitlines()

# 기록
records=lines[:n]
#단어 리스트 개수
c=int(lines[n])
# 단어 리스트 
words=lines[n+1:n+1+c]

# 중복 확인
# 앞뒤 단어 일치 확인

#기록이 1개라면 바로 정답 출력
if n==1:
    print(words[0])
else:
    idx=records.index('?')
    
    #앞뒤 단어 추출
    prev=records[idx-1] if idx>0 else ''
    next=records[idx+1] if idx+1<n else ''

    for i,word in enumerate(words):
        if word in records:
            continue #다음단어로


        if (not prev or word.startswith(prev[-1])) and (not next or word.endswith(next[0])):
            print(word)


#31120	36







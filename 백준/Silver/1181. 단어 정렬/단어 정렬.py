from collections import defaultdict
n=int(input())

words={input() for _ in range(n)}
words=list(words)

# 길이순 -> 사전순 (튜플 사용)
words.sort(key=lambda x:(len(x),x)) # 길이 순으로 정렬, 길이가 같다면 사전 순으로 정렬

for word in words:
    print(word)
from collections import defaultdict
n=int(input())

# 중복 제거를 위해 set
words=defaultdict(set)

for _ in range(n):
    word=input()
    words[len(word)].add(word)


keys=list(words.keys())
keys.sort()

for key in keys:
    word_list=list(words[key])
    word_list.sort()

    for w in word_list:
        print(w)

import sys
from itertools import combinations

input = sys.stdin.readline
word = list(input().strip())
word_length = len(word)

result = set()

for i in range(1, word_length - 1):
    for j in range(i+1, word_length):
        first = word[:i]
        sec = word[i:j]
        thrid = word[j:]

        # reverse
        first.reverse()
        sec.reverse()
        thrid.reverse()

        # 합치기
        result.add("".join(first+sec+thrid))
print(sorted(result)[0])
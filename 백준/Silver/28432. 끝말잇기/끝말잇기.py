import sys
n = int(sys.stdin.readline())

lines = sys.stdin.read().splitlines()

# 기록
records = lines[:n]
# 단어 리스트 개수
c = int(lines[n])
# 단어 리스트 
words = lines[n + 1:n + 1 + c]

if n == 1:
    print(words[0])
else:
    # '?'의 인덱스 찾기
    idx = records.index('?')

    prev = records[idx - 1] if idx > 0 else ''
    next = records[idx + 1] if idx < n - 1 else ''

    for word in words:
        if word in records:
            continue  # 다음 단어로
        if (not prev or word.startswith(prev[-1])) and (not next or word.endswith(next[0])):
            print(word)
            break  # 조건을 만족하는 단어를 찾으면 종료

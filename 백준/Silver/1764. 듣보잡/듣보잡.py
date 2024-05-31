import sys
input = sys.stdin.readline

n, m = input().rstrip().split()

# 명단 dict 생성
users = {}

for _ in range(int(n) + int(m)):
    name = input().rstrip()
    users[name] = users.get(name, 0) + 1

# value가 2인 듣보잡 찾기
result = [name for name, count in users.items() if count == 2]
result.sort()

# 출력
print(len(result))
for name in result:
    print(name)

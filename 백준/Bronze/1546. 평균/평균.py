n = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)

result = 0
for score in score_list:
    result += score / max_score * 100

print(result / n)

def solution(clothes):
    answer = 1
    fashion_map = {}
    for item, category in clothes:
        fashion_map[category] = fashion_map.get(category, 0) + 1

    for x in list(fashion_map.values()):
        answer*=(x+1)

    return answer-1
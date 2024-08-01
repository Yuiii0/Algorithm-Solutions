# 가장 맨앞 요소가 빠져나가야 다음 요소가 빠져나갈 수 있으므로 -> queue 사용
from collections import deque
def solution(cards1, cards2, goal):

    answer = ''
    first_cards=deque(cards1)
    sec_cards=deque(cards2)

    for word in goal:
        if first_cards and word==first_cards[0]:
            print(first_cards.popleft())
        elif sec_cards and word==sec_cards[0]:
            print(sec_cards.popleft())
        else:
            return 'No'
    return 'Yes'

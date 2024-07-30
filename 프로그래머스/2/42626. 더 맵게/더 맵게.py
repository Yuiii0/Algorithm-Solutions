import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while True:
        # 최소값이 k이상이되면, while 종료
        first = heapq.heappop(scoville)
        if first >= K:
            break

        if len(scoville)==0:
            return -1
        # 1,2번째 min값 섞어서 새로운 스코빌 구하기
        second = heapq.heappop(scoville)
        count += 1
        heapq.heappush(scoville, first + (second * 2))

    return count





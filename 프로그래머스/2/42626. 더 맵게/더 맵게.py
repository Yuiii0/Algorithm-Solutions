import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while len(scoville) >1:
        # pop한 값이 k이상이되면, while 종료

        min_value = heapq.heappop(scoville)
        if min_value >= K:
            return count



        # 섞어서 새로운 스코빌 구하기
        sec_min = heapq.heappop(scoville)

        new_scoville = min_value + (sec_min * 2)
        count += 1
        heapq.heappush(scoville, new_scoville)

    # 가장 안매운 스코빌이 K이상인지 확인
    if scoville[0]>=K:
        return count
    else:
        return -1




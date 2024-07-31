import heapq


def solution(operations):
    heap = []
    for operation in operations:
        [inst, value] = operation.split(' ')
        value = int(value)
        if inst == 'I':
            # heap 삽입
            heapq.heappush(heap, value)

        elif heap:
            if value > 0:
                # maxHeap을 생성하기 위해 부호 반대로 변경
                for i in range(len(heap)):
                    heap[i] = -heap[i]
                heapq.heapify(heap)
                heapq.heappop(heap)
                # 다시 부호 돌려놓기
                for i in range(len(heap)):
                    heap[i] = -heap[i]
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)


    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]













import heapq

def solution(operations):
    heap=[]
    for operation in operations:
        [inst,value]=operation.split(' ')
        if inst=='I':
            # heap삽입
            heapq.heappush(heap,int(value))

        else:
            if value=='1':
                # maxHeap으로 만들기?
                if heap:
                    for i in range(len(heap)):
                        heap[i]=-heap[i]

                    heapq.heapify(heap)

                    heapq.heappop(heap)
                    # 다시 돌려놓기
                    for i in range(len(heap)):
                        heap[i] = -heap[i]
                    heapq.heapify(heap)



            else:
                if heap:
                    heapq.heappop(heap)

    if heap:
        heap_min = heap[0]
        heap_max = sorted(heap, reverse=True)[0]
        return [heap_max, heap_min]
    else:
        return [0,0]











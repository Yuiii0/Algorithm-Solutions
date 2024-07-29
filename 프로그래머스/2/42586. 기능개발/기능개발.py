import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    progress_days=[math.ceil((100-x)/speeds[idx]) for idx,x in enumerate(progresses)]

    queue=deque(progress_days)

    done=queue[0]
    count=0

    while queue:
        if queue[0]<=done: #9<=9
            # 빠져나가도됌
            queue.popleft()
            count+=1 #2 #1
        else:
            answer.append(count) #[2]
            count = 0
            done=queue[0]
    answer.append(count)


    return answer


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)  # 대기 트럭들
    bridge = deque([0] * bridge_length)  # 다리 상태 (길이만큼 0으로 초기화)
    current_weight = 0  # 현재 다리 위의 무게 합

    while trucks or current_weight > 0:  # 대기 트럭이 있거나 다리 위에 트럭이 있는 동안 반복
        answer += 1  # 1초 경과

        # 다리에서 트럭이 나감
        current_weight -= bridge.popleft()

        if trucks:
            truck = trucks[0]  # 대기 트럭의 첫 번째 트럭
            # 다리에 트럭을 올릴 수 있는지 확인
            if current_weight + truck <= weight:
                bridge.append(trucks.popleft())  # 트럭을 다리에 올림
                current_weight += truck  # 현재 다리 위의 무게에 추가
            else:
                bridge.append(0)  # 다리에 트럭을 올리지 못함

    return answer

# 예시 테스트


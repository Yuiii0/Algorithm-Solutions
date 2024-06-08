def bubble_sort(arr):
    # 배열의 길이를 n에 저장합니다.
    n = len(arr)
    # 배열의 모든 요소를 순회합니다.
    for i in range(n):
        # 내부 루프는 배열의 끝에서 i번째 요소까지 반복합니다.
        # 이는 이미 정렬된 요소를 제외하기 위함입니다.
        for j in range(0, n-i-1):
            # 현재 요소가 다음 요소보다 크다면, 두 요소를 교환합니다.
            if arr[j] > arr[j+1]:
                # 두 요소를 교환합니다.
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 예제 데이터
data = [5, 2, 9, 1, 5, 6]
# 버블 정렬 함수를 호출하여 데이터를 정렬합니다.
bubble_sort(data)
# 정렬된 데이터를 출력합니다.
print("버블 정렬:", data)

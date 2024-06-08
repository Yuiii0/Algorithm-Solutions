def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2] #초기 pivotd은 mid값으로
    left=[x for x in arr if x<pivot] #pivot보다 작은 수 리스트
    right=[x for x in arr if x>pivot] #pivot보다 큰 수 리스트
    return quick_sort(left)+middle+quick_sort(right)

# 예제 데이터
data = [5, 2, 9, 1, 5, 6]
sorted_data = quick_sort(data)
print("퀵 정렬:", sorted_data)
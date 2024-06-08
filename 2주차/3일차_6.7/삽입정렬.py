def insertion_sort(arr):
    for i in range(1,len(arr)): #맨처음 요소는 정렬된쪽으로 간주함
        key=arr[i]
        j=i-1 #정렬된쪽의 마지막 포인터?

        # 정렬된 포인터 j
        # 확인 포인터 i
        # J>=0은 유효범위 
        # 정렬된 상태라면 j포인터가 가리키는 수가 더 작아야함 
        while j>=0 and key<arr[j]:
            # j를 하나씩 왼쪽으로 돌면서 나 여기 들어가도되나 확인함
            arr[j+1]=arr[j] #인덱스 이동
            j-=1
            arr[j+1]=key #올바른 위치에 키 삽입

data = [5, 2, 9, 1, 5, 6]
insertion_sort(data)
print("삽입 정렬:", data)
            
            
        ㄴ
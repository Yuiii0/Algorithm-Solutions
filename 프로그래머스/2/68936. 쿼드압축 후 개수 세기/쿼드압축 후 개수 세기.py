def quad(x,y,arr,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[x][y]!=arr[i][j]:
                size=size//2
                quad(x,y,arr,size)
                quad(x,y+size,arr,size)
                quad(x+size,y,arr,size)
                quad(x+size,y+size,arr,size)
                return

    answer[arr[x][y]]+=1

def solution(arr):
    global answer
    answer = [0, 0]

    quad(0, 0, arr, len(arr))
    return answer


# 좌표 정렬하기 2

# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

def Bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif arr[j][1] == arr[j+1][1]: # y값이 같다면
                if arr[j][0] > arr[j+1][0]: # x의 값을 비교
                    arr[j], arr[j+1] = arr[j+1], arr[j]

N  = int(input()) # 좌표 개수
arr = [[0]*2 for _ in range(N)]
for i in range(N): # 좌표를 입력 받기
    arr[i][0], arr[i][1] = map(int, input().split())
    
Bubble_sort(arr, N)

for i in range(N):
    print(*arr[i])



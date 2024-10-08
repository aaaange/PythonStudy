# 이동하기 https://www.acmicpc.net/problem/11048

# 문제
# 준규는 N×M 크기의 미로에 갇혀있다. 미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.
# 준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 
# 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 또, 미로 밖으로 나갈 수는 없다.
# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

# 입력
# 첫째 줄에 미로의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 1,000)
# 둘째 줄부터 N개 줄에는 총 M개의 숫자가 주어지며, r번째 줄의 c번째 수는 (r, c)에 놓여져 있는 사탕의 개수이다. 
# 사탕의 개수는 0보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력한다.

# N: 행의 수, M: 열의 수를 입력받음
N, M = map(int, input().split())

# 데이터를 저장할 리스트 초기화
data = []

# dp 배열 초기화: N x M 크기의 2차원 리스트
# dp[i][j]는 (0, 0)에서 (i, j)까지의 최댓값을 저장
dp = [[0 for c in range(M)] for r in range(N)]

# 각 행의 데이터를 입력받아 data 리스트에 추가
for i in range(N):
    data.append(list(map(int, input().split())))

# 시작점 (0, 0)의 값을 dp 배열에 초기화
dp[0][0] = data[0][0]

# dp 배열을 채우기 위한 이중 반복문
for i in range(0, N):
    for j in range(0, M):
        # (i, j)에서 오른쪽 아래 대각선으로 이동할 경우
        if i + 1 < N and j + 1 < M:
            # (i, j)에서 (i+1, j+1)로 이동할 때의 최댓값 업데이트
            dp[i + 1][j + 1] = max(dp[i][j] + data[i + 1][j + 1], dp[i + 1][j + 1])

        # (i, j)에서 아래로 이동할 경우
        if i + 1 < N:
            # (i, j)에서 (i+1, j)로 이동할 때의 최댓값 업데이트
            dp[i + 1][j] = max(dp[i][j] + data[i + 1][j], dp[i + 1][j])

        # (i, j)에서 오른쪽으로 이동할 경우
        if j + 1 < M:
            # (i, j)에서 (i, j+1)로 이동할 때의 최댓값 업데이트
            dp[i][j + 1] = max(dp[i][j] + data[i][j + 1], dp[i][j + 1])

# 최종적으로 (N-1, M-1)까지의 최댓값을 출력
print(dp[N - 1][M - 1])

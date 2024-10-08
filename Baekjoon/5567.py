# 결혼식 https://www.acmicpc.net/problem/5567

# 문제
# 상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.
# 상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. 
# (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 

# 출력
# 첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.

from collections import deque

N = int(input()) # 상근이의 동기 수
M = int(input()) # 관계 수
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0]*(N+1) # 0 ~ N까지 인덱스 만들어 주기
count = 0

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(x):
    q = deque([x])
    visited[x] = 1
    
    while q:
        friend = q.popleft()
        for people in graph[friend]:
            if visited[people] == 0:
                q.append(people)
                visited[people] = visited[friend] + 1

BFS(1)
for idx in range(2, N+1): # 1부터 시작하는 데 1은 상근이라 셀 필요 x
    if 0< visited[idx] <=3:
        count += 1

print(count)
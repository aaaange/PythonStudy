# 마인크래프트 https://www.acmicpc.net/problem/18111

# 문제
# 팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다. 
# 마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.
# 목재를 충분히 모은 lvalue는 집을 짓기로 하였다. 하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.
# lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
# 1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
# 단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

# 입력
# 첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

N, M, B = map(int, input().split()) # N 세로 길이, M 가로 길이, B 인벤토리 블럭 개수
map_list = [list(map(int, input().split())) for _ in range(N)]
# print(map_list)
h_list = []
time = 0

# 최빈값 구하기
f_list = [0] * 257 # 높이가 0부터 256까지니까 256도 세주기 위해서
for i in range(N):
    for j in range(M):
        f_list[map_list[i][j]] += 1
        h_list.append(map_list[i][j]) # 최고값 찾으려고 미리 담아두기
        
mode = f_list.index(max(f_list)) # 최빈값

def flatten(mode, B):
    global h_list, time
    if mode < 0:
        return
    mode_value = mode
    # 최빈값보다 큰 수와의 차
    for idx in range(mode,max(h_list)+1): # 최빈값부터 최대값까지만 순회시키기
        if f_list[idx] == 0: # 값이 없으면 continue
            continue 
        else:
            B += abs(mode - idx)*f_list[idx]
            time += abs(mode - idx)*f_list[idx]*2

    # 만약 최빈값이 가장 낮은 땅이었다면 함수를 끝내고, 그렇지 않다면 낮은 값을 인벤토리의 블럭으로 채워줄 수 있는지 확인
    if mode == min(h_list):
        return mode_value
    else:
        count = 0 # 채울 때 필요한 블럭 수 
        for idx_2 in range(min(h_list),mode):
            if f_list[idx_2] == 0:
                continue
            else:
                count += (mode - idx_2)*f_list[idx_2]
        if B >= count:
            time += count
            return mode_value
        else:
            return flatten(mode-1, B)

m_v = flatten(mode, B)

print(time, m_v)


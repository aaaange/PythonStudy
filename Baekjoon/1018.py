# 체스판 다시 칠하기

# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.



def count_repaints(board, start_row, start_col, first_color):
    # 첫 번째 색이 'W'인지 'B'인지에 따라 체스판을 칠하는데 필요한 비용을 계산하는 함수
    if first_color == 'W': # 첫 번째 색이 W이면
        colors = ['W', 'B'] # 이 순서로
    else : # 첫 번째 색이 B이면
        colors = ['B', 'W'] # 이 순서로 
    
    repaints = 0 # 색칠한 개수를 세는 변수 선언
    
    for i in range(8): # 행 8칸
        for j in range(8): # 열 8칸 
            expected_color = colors[(i + j) % 2] # 번갈아가며 컬러 칠하기
            if board[start_row + i][start_col + j] != expected_color: # 칠해놓은 체스판과 실제 8x8 부분이 같은 색인지 확인하고 다르면 +1
                repaints += 1
    
    return repaints # 색칠한 개수 리턴

def min_repaints_to_chessboard(board): 
    n = len(board) # 행 값
    m = len(board[0]) # 열 값
    min_repaints = float('inf') # 최초의 최소를 무한대로 설정해준다.
    
    for i in range(n - 7): # 행 값에서 7을 빼면 8x8이 들어갈 수 있는 행 값만 반복됨
        for j in range(m - 7): # 열 값에서 7을 빼면 8x8에 들어갈 수 있는 열 값만 반복됨.
            repaints_w_start = count_repaints(board, i, j, 'W') # 왼쪽 위 칸이 흰색('W')인 체스판 패턴으로 맞추기 위해 몇 개의 칸을 다시 칠해야 하는지 계산
            repaints_b_start = count_repaints(board, i, j, 'B') # 왼쪽 위 칸이 검정('B')인 체스판 패턴으로 맞추기 위해 몇 개의 칸을 다시 칠해야 하는지 계산
            # min_repaints = min(min_repaints, repaints_w_start, repaints_b_start)
            if repaints_w_start < min_repaints: # 최소값이면 넣어주기
                min_repaints = repaints_w_start
            if repaints_b_start < min_repaints: # 최소값이면 넣어주기
                min_repaints = repaints_b_start
    
    return min_repaints

# 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 최소 다시 칠해야 하는 개수 출력
print(min_repaints_to_chessboard(board))

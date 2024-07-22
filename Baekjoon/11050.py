# 이항 계수 1

# 문제
# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# \(N\)과 
# \(K\)가 주어진다. (1 ≤ 
# \(N\) ≤ 10, 0 ≤ 
# \(K\) ≤ 
# \(N\))

# 출력
 
# \(\binom{N}{K}\)를 출력한다.


# 이항계수 공식 = n! / (k! (n-k)!)

# 팩토리얼 재귀함수

def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1) # 반환 값들이 누적이 되어 있음.


input_1 = list(map(int, input().split()))

N = factorial(input_1[0]) 
K = factorial(input_1[1])
N_K = factorial(input_1[0] - input_1[1])

print(N//(K*N_K))
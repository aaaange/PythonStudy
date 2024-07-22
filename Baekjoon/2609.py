# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.


input_1 = list(map(int, input().split()))


# 소인수분해
def prime_factors(n):
    factors = []                # 소인수분해의 결과를 담을 리스트
    i = 2                       # 2 이상으로 나눠야 하니 i = 2로 시작
    while i <= n:               # i가 n과 같거나 작어자면 반복문 종료
       if n % i == 0:           # i로 나눴을 때 나머지가 없으면
           factors.append(i)    # 소인수로 list에 넣기
           n /= i               # n을 i로 나눈 몫 구함 (어짜피 나눠 떨어졌으니 /이나 //이나 같음)  
       else:
           i += 1               # i를 +1 하여 재시도
    return factors

# 입력 받은 값 소인수분해하기
one = prime_factors(input_1[0])
two = prime_factors(input_1[1])

# 최대 공약수
# 두 리스트의 공통 값 찾기 -> 교집합
intersection = list(set(one) & set(two))
# print(intersection)


# list 곱하기
def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        else:
            ans *= n
    return ans


# 최대공약수
inter_1 = multiply(intersection)
print(inter_1)


# 최소공배수
 
mul_1 = input_1[0] // inter_1
# print(mul_1)
mul_2 = input_1[1] // inter_1
# print(mul_2)

common_multiple = inter_1 * mul_1 * mul_2

print(common_multiple)
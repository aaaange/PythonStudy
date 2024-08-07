# 달팽이는 올라가고 싶다.

# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.



# A : 낮에 올라가는 높이(m)
# B : 자는 동안 미끄러지는 높이 (m) -- 정상에 올라간 후에는 미끌어지지 않음
# V : 나무 막대의 높이 (m)

import sys
input = sys.stdin.readline ## 시간 줄여주기

import math

A, B, V = map(int, input().split())

# height = A - B

result = ((V - A) / (A-B) ) + 1

# while height < V:
#     height += A
#     if height >= V:
#         break
#     else:
#         height -= B
#         Day += 1

print(math.ceil(result))
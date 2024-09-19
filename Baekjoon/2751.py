# 수 정렬하기 2 https://www.acmicpc.net/problem/2751

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

# 모든 입력을 한 번에 읽기 (여러 줄의 입력을 빠르게 처리 가능)
input = sys.stdin.read


def main():
    # 모든 입력을 한 번에 읽어오기
    data = input().split()

    # 첫 번째 줄에서 N을 추출
    N = int(data[0])

    # 나머지 데이터에서 정수를 추출
    arr = list(map(int, data[1:1 + N]))

    # 정렬
    arr.sort()

    # 정렬된 결과를 한 번에 출력(반복적인 print보다 효율적임)
    sys.stdout.write('\n'.join(map(str, arr)) + '\n')

main()


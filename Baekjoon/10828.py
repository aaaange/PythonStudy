# 스택  https://www.acmicpc.net/problem/10828

# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

class Stack:
    def __init__(self, size):
        self.stack = [None] * size  # 스택 배열 초기화
        self.top = -1  # 스택의 최상위 인덱스
        self.max_size = size  # 스택의 최대 크기

    def is_full(self):
        """
        스택이 가득 찼는지 여부를 반환합니다.
        """
        return self.top + 1 == self.max_size

    def push(self, value):
        """
        스택에 값을 추가합니다. 스택이 가득 차면 'full'을 출력합니다.
        """
        if self.is_full():
            print('full')
        else:
            self.top += 1
            self.stack[self.top] = value

    def is_empty(self):
        """
        스택이 비어있는지 여부를 반환합니다.
        """
        return self.top == -1

    def pop(self):
        """
        스택에서 값을 제거하고 반환합니다. 스택이 비어있으면 -1을 출력합니다.
        """
        if self.is_empty():
            print(-1)
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(value)

    def size(self):
        """
        현재 스택에 들어 있는 요소의 개수를 반환합니다.
        """
        return self.top + 1

    def top_value(self):
        """
        스택의 최상위 요소를 반환합니다. 스택이 비어있으면 -1을 출력합니다.
        """
        if self.is_empty():
            print(-1)
        else:
            print(self.stack[self.top])


N = int(input())  # 스택의 크기 입력

s = Stack(N)

for _ in range(N):
    command = input().strip()
    if command.startswith('push'):
        _, value = command.split()
        s.push(int(value))
    elif command == 'pop':
        s.pop()
    elif command == 'size':
        print(s.size())  # 현재 스택의 크기 출력
    elif command == 'empty':
        print(1 if s.is_empty() else 0)  # 스택이 비어있으면 1, 아니면 0
    elif command == 'top':
        s.top_value()  # 스택의 최상위 요소 출력

# 문자열 반복

# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

test_cace = int(input())
# 두번 째 줄에 들어오는 입력값을 공백을 기준으로 나누고 각 변수에 따로 넣는다. 그리고 리스트 0번은 숫자로 변경해주고(r) 1번은 그대로 둔다.(s)
# 그리고 r 숫자만큼 s의 각 글자에 곱해서 출력해주기.
# 이를 test_cace만큼 반복한다.


# for i in range(test_cace):
#     list_1 = input().split()
#     # repeat, string = input().split()
#     s = len(string)
    
#     for j in range(s):
#         output_1 = []
#         output_1 = string[j]*int(repeat)
#         print(''.join(output_1))
#     print(output_1)
#     i += 1

# for i in range(test_cace):
#     list_1 = input().split()
#     s = len(list_1[1])
    
#     for j in range(s):
#         output_1 = []
#         output_1 = list_1[1][j]*int(list_1[0])
#         print(output_1, end="")
#     i += 1


for i in range(test_cace):
    repeat, char = input().split()
    for i in range(len(char)):
        print(char[i]*int(repeat), end='')
    print()


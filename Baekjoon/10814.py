# 나이순 정렬

# 문제
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

# 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.


N = int(input())

member_list = []

for _ in range(N):
    member_list.append(input())

# print(member_list)

# # 버블정렬 응용하기
# def BubbleSort_2(a, N): # 버블 정렬 응용
#     for one in range(N-1, 0, -1): # N-1부터 0까지 역수를 준다. 
#         for two in range(one): 
#             if a[two][0:3] > a[two+1][0:3]: # 리스트의 요소들을 비교하는데 인덱스 0, 1번째 요소만 고려하여 a[two]가 더 크면
#                 a[two], a[two+1] = a[two+1], a[two] # 서로 자리를 바꿔주기
#             elif a[two][0:3] == a[two+1][0:3]: # 그러나 같으면 아무것도 하지 않고 넘기기 (왜냐면 입력순으로 줄 세워야 하기에)
#                 pass
            

# # for i in range(N):
# #     member_list[i][0:3]
# #     BubbleSort(member_list[i][0:3], N)

# BubbleSort_2(member_list, N) # 위에 만든 응용버블함수에 넣기

# for i in range(N):
#     print(member_list[i]) # 하나씩 출력하기
    
# 카운팅정렬

COUNTS = [0] * N
TEMP = [0] * N

# 1단계 : member_list 원소 별 개수 세기
for x in member_list:
    COUNTS[x[0:3]]

print(COUNTS)
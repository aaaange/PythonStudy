# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

# n = int(input()) # 앞으로 입력될 알파벳의 개수
# my_list = []

# for x in range(n): # 반복적으로 알파벳을 담는 함수
#     my_list.append(input())

# # 중복 제거하기
# your_list = [] # 중복 제거한 값들을 담아줄 리스트

# for x in my_list: # 중복 제거해서 담기
#     if x not in your_list:
#         your_list.append(x)
# # print(your_list)

# # 정렬하기
# # 1단계 : your_list 원소 별 개수 세기
# counts = [0] * len(my_list)
# for x in your_list: # 인덱스 번호와 값이 일치하는지 확인하고 일치하면 숫자 업
#     for i in range(len(your_list)):
#         if x == counts[i]:
#             counts[i] += 1

# # 2단계 : 각 원소까지의 누적 개수 구하기
# for i in range(1, len(my_list)):
#     counts[i] = counts[i-1] + counts[i]

# # 3단계 : your_list의 맨 뒤부터 TEMP에 자리 잡기
# temp = [] * len(your_list)
# for i in range(len(your_list)-1, -1, -1):
#     counts[your_list[i]] -= 1
#     temp[counts[your_list[i]]] = your_list[i]

# print(temp)
    

# 길이 측정하기
# len_list = []
# for i in range(len(your_list)): # 값 개수만큼 반복
#     len_list.append(your_list[i])
    

# 버블 함수를 이용한 방법 -> 시간 초과
n = int(input())  # 단어의 개수
my_list = [] 

for _ in range(n):
    my_list.append(input())

# 중복 제거
unique_list = list(set(my_list))

# 버블 정렬을 사용하여 정렬 (길이와 사전 순으로)
for i in range(len(unique_list)): # 중복 제거한 리스트 길이 만큼 반복 
    for j in range(0, len(unique_list) - i - 1): # 0부터 중복 제거 리스트 길이 - i - 1
        # 두 단어를 비교하여 정렬 기준에 따라 교환
        if len(unique_list[j]) > len(unique_list[j + 1]) or ( # 길이가 짧은게 앞으로 오게 
                len(unique_list[j]) == len(unique_list[j + 1]) and unique_list[j] > unique_list[j + 1]): # 길이가 같으면 사전 순으로 앞으로 오게
            # 두 단어를 교환
            unique_list[j], unique_list[j + 1] = unique_list[j + 1], unique_list[j]

# 정렬된 단어들을 출력
for word in unique_list:
    print(word)



# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.


input1 = int(input())
input2 = list(map(int,input().split())) # list를 숫자형으로 변경하기

answer = []
answer.append(min(input2))
answer.append(max(input2))

# for i in range(input1):
#     if input2[i] == min(input2):
#         answer.append(input2[i]) #리스트이름.append(추가할 것) > 리스트 맨 뒤에 데이터 추가하기
#     if input2[i] == max(input2):
#         answer.append(input2[i])

answer2 = " ".join(str(s) for s in answer) #문자열 합치기는 문자만 가능한 것 같음 > 숫자를 문자로 바꿔주었음
print(answer2)



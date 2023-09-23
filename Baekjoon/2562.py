# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 10개의 자연수의 구분이 엔터임.
# input = input() # 한 줄, 즉 엔터를 기점으로 한 줄을 가져오는 함수



# when
listData = []
for i in range(10):
    listData.append(int(input()))
    
# print(listData)



# then
def is_i_greaterthen_j(i, j) -> bool:
    return i > j
max = 0 # 최댓값
line = 0 # 해당 데이터가 있던 줄

# [13123, 232324, 23555, 21323, 1, 23, 3, 4, 256634, 2]
for index, data in enumerate(listData): # enumerate(데이터) -> 인덱스와 데이터를 같이 반환해줌 
    if data > max:
        max = data
        line = index + 1

# finally
print(max)
print(line)
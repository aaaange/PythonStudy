# 좌표 정렬하기

# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.



# ## 버블정렬로 풀기 -> 점의 개수가 많을 때 비효율적

# N = int(input()) # 점의 개수 

# my_list = []
# for i in range(N): # 점의 좌표 받아주기
#     my_list.append(input())

# for i in range(N-1,0,-1): # 버블 정렬 사용하여 정렬하기
#     for j in range(0,i):
#         if my_list[j] > my_list[j+1]:
            
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            
# for i in range(N): # 순서대로 출력하기
#     print(my_list[i])


## sort 사용하기

N = int(input()) # 점의 개수 

my_list = []
for i in range(N): # 점의 좌표 받아주기
    x, y = map(int, input().split())
    my_list.append((x,y))

my_list.sort()

for x, y in my_list: # 순서대로 출력하기
    print(x,y)

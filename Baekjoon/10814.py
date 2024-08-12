# 나이순 정렬

# 문제
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

# 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.


N = int(input())

# 퀵정렬 응용
def quick_sort(arr):
    # 리스트의 길이가 1 이하이면, 이미 정렬된 상태이므로 바로 반환
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택 (첫 번째 요소 선택)
    pivot = arr[len(arr) // 2]
    
    left = [] # 피벗보다 작은 요소들을 담을 리스트
    middle = []  # 피벗과 같은 요소들을 담을 리스트
    right = []  # 피벗보다 큰 요소들을 담을 리스트
    
    for element in arr:
        # 나이 비교 -> 나이가 같다면 입력 순서 유지 (안정정렬)
        if element[0] < pivot[0]:  # 나이 비교
            left.append(element)
        elif element[0] == pivot[0]:
            middle.append(element)  # 나이가 같으면 middle에 추가
        else:
            right.append(element)   # 나이가 크면 right에 추가
    
    return quick_sort(left) + middle + quick_sort(right)

# 입력 받을 리스트
member_list = []

# 데이터 입력받기
for _ in range(N):
    user_input = input() 
    
    # 입력을 공백 기준으로 나누어 나이와 이름을 추출
    age, name = user_input.split()
    
    # 나이를 정수로 변환하고 튜플로 저장
    member_list.append((int(age), name))

# 정렬 수행
sorted_data = quick_sort(member_list)

# 결과 출력
for age, name in sorted_data:
    print(age, name)

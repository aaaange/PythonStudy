# 요세푸스 문제 0

# 문제
# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

N, K = map(int, input().split()) # N : 인원 수, K : 뽑을 번호

count = 0 # K번째를 뽑아내기 위한 변수
member = [] # 이거 한 줄로 작성하는 것 알아보기
for x in range(1, N+1): # 1에서 N까지의 사람들을 list에 하나씩 담아주기 위한 for문
    member.append(x)
result = [] # 결과 값을 담아줄 리스트

while len(result) < N: # 결과 값의 길이가 최대 인원보다 작은 동안만 돌아가는 반복문
    for i in range(N): # 0에서 N-1을 반복
        if member[i] != 0: # 만약 i번째 멤버가 0이 아니라면
            count += 1 # count를 하나 올려준다. 왜냐하면 빈 값을 0을 넣어줄 것이기 때문
            if (count % K) == 0: # 카운트를 K로 나눈 나머지가 0이라면(즉, 지금이 K번째 순서라면)
                result.append(member[i]) # 결과 값을 담아줄 리스트에 해당 멤버를 추가
                member[i] = 0 # 그리고 그 자리를 0으로 둔다.
                count = 0 # 카운트를 초기화 한다. (엇 그러면 위에 K로 나눈 나머지.. 이거 안쓰고 그냥 카운트는 K라면도 가능했겠다.)

print(f'<', end = '') # 꺾인 괄호를 넣고 줄바꿈을 없애줌.
print(*result, sep = ', ', end = '') # 결과 리스트를 언패킹하고 구분자로 ','를 지정, 줄바꿈 제거
print(f'>') # 꺾인 괄호 넣기


            


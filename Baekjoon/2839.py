# 설탕 배달

# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

def sugar_div(namerge):
    global count
    if namerge < 3: # 나머지가 3보다 작으면 나눌 수 없으므로 리턴
        return -1
    elif namerge == 0: # 나머지가 0이면 
        return count # count를 리턴
    else: # 아직 나눌 수 있다면
        if namerge % 3 == 0: # 나머지가 3으로 나누어 떨어질 때
            count += namerge // 3 # 몫을 카운팅
            namerge %= 3 # 나머지를 다시 재할당
            return count # 카운트 리턴
        else: # 3으로 나누어 떨어지지 않을 때
            count -= 1 # 5kg 짜리 봉지 하나 빼고
            namerge += 5 # 나머지에 5 추가 
            return sugar_div(namerge) # 반복


N = int(input())

sugar = [5, 3] # 설탕 봉지가 5kg, 3kg짜리가 있음

count = 0 # 배달 해야 할 봉지 수
count3 = 0

# 5kg 봉지 먼저 세보기
if N >= 5:
    count += N // sugar[0]
    namerge = N % sugar[0]
    result = sugar_div(namerge) # 3으로 나누는 것은 함수로
    print(result)
else:
    if N == 3:
        print(1)
    else:
        print(-1)
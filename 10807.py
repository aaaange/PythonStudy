input1 = int(input())
input2 = input().split()
input3 = int(input())

#input3과 input2에 들어있는 숫자 매칭해보면서(반복) 개수 세기..?
#

# while i < input1+1:
#     if input3 == input2[i]:
#         print(count())

i = 0
cnt = 0 
while i < input1:
    if(int(input2[i]) == input3):
        cnt = cnt+1
    i = i+1




print(cnt)

# list_a = list(map(int, input2))
# print(list_a.count(input3))



# input2.count(input3)





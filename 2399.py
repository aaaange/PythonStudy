

# input1 = input()
# input2 = input()

# splitData = input2.split(" ")

# n = int(input1)
# # n**2-n

# i = 0
# j = 0 
# list1 = []
# while i < n:
#     while j < n:
#         list1.append(abs(int(splitData[i]) - int(splitData[j])))
#         j += 1
#     i += 1
# print(list1)


n = int(input())
x = list(map(int, input().split()))
x.sort()

total = 0
for i in range(1, n):
    total += (x[i] - x[i - 1]) * i * (n - i)

print(total * 2)

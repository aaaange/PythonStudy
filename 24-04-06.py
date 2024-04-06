#데이터를 다루려면 데이터를 저장해야 함.
Numeric_data = 1
String_data = '안녕'
Array_data = [1, 2, 3, 4]
Dictionary_data = {
    "이름":"김동호",
    "성별":"남자"
}

print(Numeric_data)
print(Dictionary_data['이름'])
print(Array_data[2])


Numeric_data = 2
# 데이터 변경은 이렇게

# 조건문, 반복문을 통해 데이터의 흐름을 논리적으로 관리

if Dictionary_data['성별'] == '남자':
    print("여성만 사용 가능한 도구입니다.")

for idx, a in enumerate(Array_data):
    print(idx ,"번째 데이터는 : ", a)
    
for idx, a in enumerate(Array_data):
    if idx == 2:
        print("세 번째 데이터에 접근했음.")
    else:
        print("세 번째 데이터가 아님")
        
# 데이터 다루는 기능을 재사용 하고, 정규화 하고싶어
def sum_array(arr):
    total = 0
    for var in arr:
        total += var
    return total

print(sum_array(Array_data))
print(sum_array([1, 2, 3, 5]))

# 데이터를 구조화 해서 정보를 저장하고 싶어.
class Human():
    def __init__(self, name, age): # 복습을 해두면 좋을 듯. (class를 안써도 Python은 쓸 수 있음.)
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
Dongho = Human('김동호', 25)
AYeong = Human('이아영', 25)

print(Dongho.get_age())
print(AYeong.get_name())


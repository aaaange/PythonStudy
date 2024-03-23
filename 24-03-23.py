data = [1, 2, 3, 4, 5] # list

print(type(data))



# Agenda
# Numpy 기본 사용법
# Pandas 기본 사용법
# 데이터 수집(API, 크롤링 등등)

# Numpy

# 파이썬에서 행렬을 다루는 라이브러리
import numpy as np

# array (배열)
# numpy를 사용하게 되면, 연산 속도를 조금 더 확보할 수 있으며, 여러 벡터 연신이나 행렬곱, 행렬 연산을 쉽게 할 수 있다.

arr = np.array([[-1, -2, -3, -4, -5], [5, 6, 7, 8, 9]])
print(type(arr))

arr = arr.__abs__() # 절대값

print(arr)


# Pandas


# 판다스 선언
import pandas as pd

# read csv

# pandas csv뿐만 아니라 여러가지 데이터 형식을 지원한다.
# read_csv, read_excel, read_json, read_sql, read_html, read_pickle, read_clipboard, read_hdf, read_feather, read_parquet, read_msgpack, read_stata, read_sas, read_spss, read_gbq, read_sql_table, read_sql_query, read_google, read_table, read_fwf, read_clipboard
data = pd.read_csv('~/paypal_bulk.csv')


print(data.head())

# 데이터 컬럼 확인
print(data.columns)

# 내가 원하는 컬럼만 가져오기.
print(data['primary_email_alias'])

# 데이터의 통계적 정보 확인
print(data.describe())

# ccType의 값을 기준으로 표준편차 도출
print(data.groupby('ccType').std())

# 데이터의 결측치 확인
print(data.isnull().sum())

# 데이터의 결측치를 채우기
data = data.fillna('임의 값')

print(data)

# 데이터 수집

# API를 호출을 해보고, 호출한 데이터를 가져와서, 가공 -> pandas로 여러가지 분석을 해보자.
import requests
import json

# API = Application Programming Interface

# 예시용 데이터 API https://www.data.go.kr/iim/api/selectAPIAcountView.do#/

# Response의 값의 번호에 따라 결과를 확인할 수 있다.
# 성공 2xx
# 실패 4xx, 5xx
# 4xx : 내 잘못.  내가 요청을 잘못했을 경우
# 5xx : 서버 잘못. 서버가 잘못했을 경우

# API 호출
# API를 호출할 때, Base URL + URI + Query String

# query string K=V

# Base URL : https://api.odcloud.kr/api
# 사용할 API의 URI : /15020770/v1/uddi:188de284-1d0b-4d81-bc1c-ec31c123edb2
result = requests.get('https://api.odcloud.kr/api/15020770/v1/uddi:188de284-1d0b-4d81-bc1c-ec31c123edb2?serviceKey=lPg2on4CWi%2FB13pfX5nWSeWyOaY7YSp5KOV%2B5Sd58W%2FCp37nhS5hHN9z6N2gBTS%2Fpj34dyyAge2j%2F%2FcVe4ix0A%3D%3D&page=0&perPage=10')
# 호출한 json을 이쁘게 보고싶다. https://jsonformatter.org/json-pretty-print

# print(result)
# # 내가 호출한 API의 결과를 확인
# print(result.text)

#내가 호출한 api의 데이터를 json으로 저장하겠다.
json_res = result.json()

# print(json_res)
result_data = json_res['data']
# print(result_data)


# 전처리
# str, json 둘 다 자료형
class 중소기업펀드정보: # 정보를 담을 클래스
    def __init__(self, result_json):
        self.운용사명:str = result_json['운용사명']
        self.상품명:str = result_json['상품명']
        self.누적수익율1개월:float = float(result_json['1개월누적수익률(퍼센트)'])
        self.누적수익율3개월:float = float(result_json['3개월누적수익률(퍼센트)'])
        self.누적수익율6개월:float = float(result_json['6개월누적수익률(퍼센트)'])
        self.누적수익율12개월:float = float(result_json['12개월누적수익률(퍼센트)'])
        self.펀드등급:int = result_json['펀드등급']
        self.펀드유형:str = result_json['펀드유형']
        self.선취수수료율:float = float(result_json['선취수수료(퍼센트)'])
        self.총보수:float = float(result_json['총보수(퍼센트)'])

    def JSON으로_출력하기(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    
# json.dumps(넣을 데이터)
# 데이터를 json '자료형'으로 바꿔준다.

# json.loads(문자열 데이터)
# '문자열 데이터'를 json '자료형'으로 바꿔준다.

        
def 전처리_결과를_판다스로_바꾸기(바꿀데이터:list):    
    전처리결과 = [] # list [json, json, json] -> json
    for i in 바꿀데이터:
        전처리결과.append(json.loads(중소기업펀드정보(i).JSON으로_출력하기()))
    return pd.DataFrame(전처리결과)

# parse list[json, json, json] to json array
# json.loads(json.dumps(중소기업펀드정보(i).JSON으로_출력하기()))
# can you parse if class does not have .JSON으로_출력하기() method?
# json.loads(json.dumps(i))

class 데이터불러오는기능:
    def __init__(self, 기본주소, 기본uri, 인증키):
        self.기본주소 = 기본주소
        self.기본uri = 기본uri
        self.인증키 = 인증키
    
    def 데이터_요청하기(self, page, size):
        return requests.get(f'{self.기본주소}{self.기본uri}?serviceKey={self.인증키}&page={page}&perPage={size}').json()['data']
    
데이터부르는기능 = 데이터불러오는기능('https://api.odcloud.kr/api', '/15020770/v1/uddi:188de284-1d0b-4d81-bc1c-ec31c123edb2', 'lPg2on4CWi%2FB13pfX5nWSeWyOaY7YSp5KOV%2B5Sd58W%2FCp37nhS5hHN9z6N2gBTS%2Fpj34dyyAge2j%2F%2FcVe4ix0A%3D%3D')

데이터요청결과 = 데이터부르는기능.데이터_요청하기(0, 100) # data 100개 list[json, json]
두번째요청결과 = 데이터부르는기능.데이터_요청하기(1, 100)
세번째요청결과 = 데이터부르는기능.데이터_요청하기(2, 100)
네번째요청결과 = 데이터부르는기능.데이터_요청하기(3, 100)

첫번째데이터요청결과판다스로바꾼거 = 전처리_결과를_판다스로_바꾸기(데이터요청결과)
두번째데이터요청결과판다스로바꾼거 = 전처리_결과를_판다스로_바꾸기(두번째요청결과)
세번째데이터요청결과판다스로바꾼거 = 전처리_결과를_판다스로_바꾸기(세번째요청결과)
네번째데이터요청결과판다스로바꾼거 = 전처리_결과를_판다스로_바꾸기(네번째요청결과)


import time
start = time.time()
print(첫번째데이터요청결과판다스로바꾼거['누적수익율12개월'].mean())
print("걸린 시간 : ", time.time() - start)
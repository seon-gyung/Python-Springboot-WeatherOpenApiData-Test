# requests 모듈 사용하여 dict 타입으로 공공데이터 다운 받기
# 다운 받은 데이터를 mariaDB에 insert하기
# 스프링 부트에서 수집한 데이터 요청할 수 있는 Controller 만들기
# HTML 부트스트랩을 이용하여 수집한 데이터 출력하기

# python -m pip install requests
# python -m pip install pymysql

import requests
from pymysql import connect, cursors

# DB 연결 설정
conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"
)

# 공공데이터 url
url = "http://openapi.seoul.go.kr:8088/576668796b646c7431333066546b7a61/json/RealtimeCityAir/1/25/"

# requests로 url 가져와서 response에 담기
response = requests.get(url)
# print(response.text) 

if response.status_code == 200:
    # 전체 데이터 json으로 담고
    jsonData = response.json()
    # print(jsonData)

    # 필요한 데이터만 뽑아서 담기
    data = jsonData.get("RealtimeCityAir").get("row")
    # print(data)

    cursors = conn.cursor(cursors.DictCursor) # 기본 전략이 tuple 타입이므로 dict 타입으로 전략 변경

    # DB에 insert하기
    insert_sql = "INSERT INTO weather (msrdt, msrrgn_nm, msrste_nm, pm10, pm25, o3, no2, co, so2, idex_nm, idex_mvl, arplt_main) VALUES (%(MSRDT)s, %(MSRRGN_NM)s, %(MSRSTE_NM)s, %(PM10)s, %(PM25)s, %(O3)s, %(NO2)s, %(CO)s, %(SO2)s, %(IDEX_NM)s, %(IDEX_MVL)s, %(ARPLT_MAIN)s);"
    cursors.executemany(insert_sql, data) # 버퍼로 쿼리 전송

    conn.commit()




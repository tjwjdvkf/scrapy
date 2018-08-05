import sqlite3
#import simplejson as json
import datetime

'''
SQLlite GUI developer
https://sqlitebrowser.org/ 

바이너리 형식으로 저장되기 때문에 설치 요망 

RDBMS 기본적으로 DDL, DML, DCL 제공
장점 : 코어 요량 220K
       빠름
       크로스 플랫폼 
'''

# DB 생성 저장 파일
conn = sqlite3.connect("C:/study/scrapy36/hanbit_media/dbfile/sqlite1.db")

# AutoCommit 
# conn = sqlite3.connect("C:/study/scrapy36/hanbit_media/dbfile/sqlite1.db" , isolation_level=None)

# DB생성 메모리(DB)
# conn = sqlite3.connect(":memory:")


# 날짜 생성

now  = datetime.datetime.now()
print('now',now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

# SQLite version 
print('sqlite3.version',sqlite3.version)

# SQLite Core Version
print('SQLite Core version', sqlite3.sqlite_version) 


#Cursor 연결
c = conn.cursor()
print(type(c))

# 테이블 생성 (SQLite3 Datatype : TEXT , NUMERIC, INTEGER, REAL, BLOB))
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY , username text, regdate text )")

# 데이터 삽입
'''
튜플 형식으로 데이터를 넣음 
주의사항 끝에 , 를 찍어줘야함
파일 실행 시 데이터 확인 
데이터 없음
커밋을 하지 않았기 때문  AutoCommit 처리를 하던, 커밋 잊지말것

'''
# c.execute("INSERT INTO users VALUES(1,'seojh',?)",(nowDatetime,))

# conn.commit()

# list 삽입
userList  = (
    (2,'seojh',nowDatetime),
    (3,'test1',nowDatetime),
    (4,'test2',nowDatetime)
)

c.executemany("INSERT INTO USERS(id, username, regdate) VALUES(?,?,?)",userList)

conn.commit()

# 리소스 반환
conn.close()
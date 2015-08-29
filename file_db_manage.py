__author__ = 'jinheesang'

import random
import sqlite3
import datetime



class Db:
    def make_file(self): #파일 (ex.20150829_DATA)들을 생성합니다. 파일 이름은 오늘 날짜부터 하루씩 증가됩니다
        for i in range(10): #만들 파일개수
            file_name = datetime.datetime.now()+datetime.timedelta(days=i) #파일이름을 하루씩 증가
            file_name = file_name.strftime("%Y%m%d")
            for j in range(20):  #파일속 데이터 개수
                data = self.select_num()
                file_text = datetime.datetime.now()+datetime.timedelta(minutes=j)+datetime.timedelta(days=i) #파일속 데이터는 파일이름과 같은 날짜에 1분씩 증가
                file_text = file_text.strftime("%Y%m%d%H%M")
                data['DATA_DATE'] = file_text

                self.file_name = str(file_name)+'_DATA' #파일이름 = 현재날짜 + _DATA
                with open(self.file_name, 'a') as f:
                    f.write(str(data)+'\n')

    def read_file(self): #make_file에서 만든 파일을 읽는다
        lines=[]
        file_now = datetime.datetime.now() #현재 요일로 된 파일부터 시작해서 하루씩 증가된 파일이름을 찾음(ex. 20150829_DATA.txt -> 20150830_DATA.txt ...)
        file_name = file_now.strftime("%Y%m%d")
        self.file_name = str(file_name)+'_DATA'
        while True: #파일이 있을때까지 반복해서 찾음
            #print(self.file_name)
            try:
                with open(self.file_name, 'r') as f:
                    lines += f.readlines()
                file_now = file_now+datetime.timedelta(days=1)
                file_name = file_now.strftime("%Y%m%d")
                self.file_name = str(file_name)+'_DATA'

            except FileNotFoundError: #하루씩 증가시키면서 파일이름을 찾을때 파일이 없으면 중지
                break

        self.insert_db(lines)

            #=================== 위는 파일 만들기, 읽기 // 아래는 DB로 옮기기

    def __init__(self,file_name):
        '''
        adasdasd
        dsdsdsadasdasdasdasda
        '''
        self.conn = sqlite3.connect(file_name)    # pets.db 생성
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS temp")
        self.cursor.execute('''CREATE TABLE temp (
        DATA_DATE DATE,
        TEMP VARCHAR(4),
        HUMI VARCHAR(4),
        ASTO VARCHAR(4))''')

        self.conn.commit()

    def execute_db(self,data1):

        self.query = "INSERT INTO temp VALUES ('{DATA_DATE}','{TEMP}', '{HUMI}', '{ASTO}')".format_map(data1)
        self.cursor.execute(self.query)
        self.conn.commit()


    def show_db(self):
        self.cursor.execute('select * from temp')
        for rec in self.cursor.fetchall():
            print(rec)

    def select_num(self): #파일을 만들때 필요한 데이터를 랜덤으로 부여

        a = random.randrange(1,10000)
        b = random.randrange(1,10000)
        c = random.randrange(1,10000)
        data = {
        'DATA_DATE' : 0,
        'TEMP' : str(a),
        'HUMI' : str(b),
        'ASTO': str(c)
        }

        return data

    def insert_db(self,lines): #파일을 읽을때    {' ...  '}  형태로 된 문자열 을그대로 사전형으로 바꿔준다
        for i in lines:
            self.execute_db(eval(i))




db = Db('a.db')

db.create_table() ##db 테이블을 만든다

db.make_file() #파일들을 만든다 (시간과 관련)

db.read_file() #만든 파일들을 읽어서 DB에 넣는다

db.show_db() #현재 DB에 저장된 목록을 보여준다


# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-


class select_num:
    def __init__(self):
        self.num = 0

    def insert(self):
        while True:
            insert = input(' >>  ')
            try:
                insert = int(insert)
                if(3>=insert and insert>=1):
                    return insert
            except ValueError:
                continue

class data_manage:
    def __init__(self):
        self.data = 0

    def data_insert(self):
        d=[]
        d.append(input('책 이름을 입력해주세요 >>   '))
        d.append(input('저자를 입력해주세요 >>   '))
        d.append(input('가격을 입력해주세요 >>   '))

        with open('data.txt', 'a' ) as f:
            for i in [0,1,2]:
                f.write(d[i])
                f.write(' ')
            f.write('\n')
        return

    def data_load(self):
        try:
            with open('data.txt', 'r' ) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
        except FileNotFoundError:
            pass


while True:
    print('학생 관리 프로그램입니다')
    print('무엇을 하시겠습니까?')
    print('\n1.입력  2.불러오기  3.프로그램 종료')

    sel = select_num()
    sel = sel.insert()

    data = data_manage()

    if(sel==1):
        data.data_insert()

    elif(sel==2):
        data.data_load()

    elif(sel==3):
        exit(1)


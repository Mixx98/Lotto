# https://dhlottery.co.kr/gameResult.do?method=byWin
# 위 사이트에서 1회부터 최신회까지의 엑셀파일을 받은다음 excel.csv로 같은 폴더에 변환해주세요!!

import pandas as pd
import random as rd
import os

def compare(NUM,numList):
    count=0
    NUM=list(NUM)
    print(NUM)

def pick(f,n):
    arr=[]
    for i in range(n):
        while(1):
            num = int(table.iat[rd.randrange(0,len(table)),rd.randrange(0,6)])
            arr.append(num)
            numList=list(set(arr))
            if(len(numList)==6):
                break
        arr.clear()
        numList.sort()
        print(">>",numList)
        f.write(str(numList)+"\n")
        

def mode_1():
    n = int(input("몇 개 필요하신가요?\n>> "))
    print("")

    f_path = "list.txt"
    if(os.path.isfile(f_path)):
        save=int(input("1. 새로 저장하실건가요?\n2. 기존의 번호에 추가하실건가요?\n>> "))
        print("")
        if(save==1):
            with open("list.txt","w") as f:
                pick(f,n)
        elif(save==2):
            with open("list.txt","a") as f:
                pick(f,n)
        else:
            print("다시 입력해 주세요")
    else:
        with open("list.txt","w") as f:
            pick(f,n)
    

def mode_2():
    f_path = "list.txt"
    if(os.path.isfile(f_path)):
        NUM = input("당첨 번호를 입력해 주세요(1,2,3,4,5,6)\n>> ")
        NUM.maketrans({
         ',': '',
         ' ': '',
         '[': '',
         ']': '',
        })
        with open("list.txt","r") as f:
            numList=f.readlines()
        compare(NUM.translate(NUM),numList)
        
    else:
        print("저장되어 있는 번호가 없습니다.")


def mode_3():
    f_path = "list.txt"
    if(os.path.isfile(f_path)):
        with open("list.txt","r") as f:
            numLists = f.read()
            print(numLists)
    else:
        print("저장되어 있는 번호가 없습니다.")

table = pd.read_csv('./excel.csv',encoding='euc-kr',header=None)
table=table.iloc[3:,13:19]
mode=0

while(1):
    mode = int(input("\n1. 번호 뽑기\n2. 번호 비교하기\n3. 저장된 번호 보기\n4. 종료\n>> "))
    print("")

    if(mode==1):
        mode_1()
    elif(mode==2):
        mode_2()
    elif(mode==3):
        mode_3()
    elif(mode==4):
        break
    else:
        print("다시 입력해 주세요\n")



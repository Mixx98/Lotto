# https://dhlottery.co.kr/gameResult.do?method=byWin
# 위 사이트에서 1회부터 최신회까지의 엑셀파일을 받은다음 excel.csv로 같은 폴더에 변환해주세요!!

import pandas as pd
import random as rd
import os

def rank(count,NUM_b): #등수를 구해주는 함수
    if(count==6):
        return "\033[31m1등\033[0m"
    elif(count==5):
        if(NUM_b!=-1):
            return "\033[31m2등\033[0m"
        else:
            return "\033[31m3등\033[0m"
    elif(count==4):
        return "\033[31m4등\033[0m"
    elif(count==3):
        return "\033[31m5등\033[0m"
    else:
        return "꽝"

def compare(NUM,NUM_b,numList): #당첨번호와 저장된 번호들을 비교하는 함수
    count=0
    NUM=list(NUM)
    print("")
    for i in numList:
        i2=i.replace('[', ' ').replace(']', ',')
        i=i.rstrip('\n')
        for j in range(6):
            if(i2.find(' '+NUM[j]+',')!=-1):
                count+=1
        print(i+" >> "+rank(count,i.find(NUM_b)))
        count=0
    

def pick(f,n): #랜덤한 6자리를 뽑아주는 함수
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
        

def mode_1(): #랜덤한 6자리 번호를 뽑고 저장하는 함수
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
    

def mode_2(): #저장된 번호들을 당첨번호와 비교하는 함수
    f_path = "list.txt"

    if(os.path.isfile(f_path)):
        NUM = input("당첨 번호 6개를 입력해 주세요(1,2,3,4,5,6)\n>> ")
        NUM_b = input("\n보너스 번호 를 입력해 주세요\n>> ")

        NUM=NUM.replace(' ', '').split(',')
        
        with open("list.txt","r") as f:
            numList=f.readlines()
        compare(NUM,NUM_b,numList)
        
    else:
        print("저장되어 있는 번호가 없습니다.")


def mode_3(): #저장된 번호들을 출력하는 함수
    f_path = "list.txt"

    if(os.path.isfile(f_path)):
        with open("list.txt","r") as f:
            numLists = f.read()
            print(numLists.rstrip('\n'))
    else:
        print("저장되어 있는 번호가 없습니다.")


#--------------------------------------------------------------------------------
#메인함수

table = pd.read_csv('./excel.csv',encoding='euc-kr',header=None)
table=table.iloc[3:,13:19]
mode=0

while(1):
    mode = input("\n\n1. 번호 뽑기\n2. 번호 비교하기\n3. 저장된 번호 보기\n4. 종료\n>> ")
    print("")

    if(mode=='1'):
        mode_1()
    elif(mode=='2'):
        mode_2()
    elif(mode=='3'):
        mode_3()
    elif(mode=='4'):
        break
    else:
        print("다시 입력해 주세요")



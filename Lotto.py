import pandas as pd
import random as rd

def mode_1():
    list=[]
    
    n = int(input("\n몇 개 필요하신가요?\n>> "))
    print()

    for i in range(1,n+1):
        for j in range(6):
            num = int(table.iat[rd.randrange(0,len(table)),rd.randrange(0,6)])
            list.append(num)
        print(i,list)
        list.clear()
    print()


table = pd.read_csv('./excel.csv',encoding='euc-kr',header=None)
table=table.iloc[3:,13:19]
mode=0

while(1):
    mode = int(input("1. 번호 뽑기\n2. 번호 비교하기\n3. 저장된 번호 보기\n4. 종료\n>> "))

    if(mode==1):
        mode_1()
    elif(mode==2):
        continue
        #mode_2()
    elif(mode==3):
        continue
        #mode_3()
    elif(mode==4):
        break
    else:
        print("다시 입력해 주세요\n")



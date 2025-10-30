from tkinter import *

def print_fields():



root=Tk() #Tkinter 윈도우 생성
Label(root, text="아이디").grid(row=0) #아이디와 패스워드 라벨 생성 및 배치
Label(root, text="비밀번호").grid(row=1)

# 아이디와 패스워드 입력 위젯 생성 및 배치
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)




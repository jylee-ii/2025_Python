from tkinter import *

class Person:
    def __init__(self, name):
        self.name=name

# is-a 관계
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes=[]
    
    # 과목 리스트에 추가
    def enrollCourse(self, subject):
        self.classes.append(subject)

    # 과목 리스트 초기화
    def clearCourses(self):
        self.classes.clear()

# 객체 생성
root=Tk()
root.title("문제4")
root.geometry("380x280")

stu=Student("홍길동")
title=Label(root, text=f"학생: {stu.name}").pack(pady=6)

# 체크버튼 프레임
f=Frame(root)
f.pack(pady=6, anchor="center")

# 체크버튼 상태 저장
var_py = IntVar(value=0)
var_ai = IntVar(value=0)
var_ds = IntVar(value=0)

# 체크버튼 생성
cb1=Checkbutton(f, text="Python",  variable=var_py)
cb2=Checkbutton(f, text="AI",  variable=var_ai)
cb3=Checkbutton(f, text="DataScience",  variable=var_ds)

# grid으로 배치
cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

# 결과 표시 라벨
result=StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb=Label(root, textvariable=result)
lb.pack(pady=6)

# 동작 함수들
def register_courses():
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

# 버튼 프레임   
btn_f=Frame(root)
btn_f.pack(pady=6)

# 버튼 배치
Button(btn_f, text="등록하기", command=register_courses).pack(side="left", padx=6)
Button(btn_f, text="초기화", command=reset_all).pack(side="left", padx=6)

root.mainloop()
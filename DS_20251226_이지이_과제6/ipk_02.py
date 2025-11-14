import tkinter as tk

class Pet:
    def speak(self):
        return "..."

# is-a
class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

# has-a
class Person:
    def __init__(self, name, pet=None):
        self.name=name
        self.pet=pet


# 객체 생성
root=tk.Tk()
root.title("문제2")
root.geometry("400x200")


# 라벨 생성
tk.Label(root, text="동물을 선택해주세요.").pack(pady=10)

# 현재 사람 객체
person=Person("홍길동")

# 버튼 정의
def select_dog():
    person.pet=Dog()
    result.set("강아지를 선택했습니다.")

def select_cat():
    person.pet=Cat()
    result.set("고양이를 선택했습니다.")

def speak():
    result.set(f"{person.name}의 반려동물 -> {person.pet.speak()}")

# 버튼 프레임
f=tk.Frame(root)
f.pack(pady=10)

# 버튼 배치
tk.Button(f, text="강아지 선택", command=select_dog).pack(side="left", padx=8)
tk.Button(f, text="고양이 선택", command=select_cat).pack(side="left", padx=8)
tk.Button(root, text="말하기", command=speak).pack(pady=10)

# 결과 표시
result=tk.StringVar(value="")
speak_label=tk.Label(root, textvariable=result, fg="blue").pack(pady=10)

root.mainloop()
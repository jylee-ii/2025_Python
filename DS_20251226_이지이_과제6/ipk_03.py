import tkinter as tk
import math

class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
    def draw(self, canvas):
        raise NotImplementedError
 
class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w*self.h)
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.h, fill="tomato")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r=r
    def area(self):
        return math.pi*self.r
    def perimeter(self):
        return 2*math.pi*self.r
    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x + self.r, self.y + self.r, fill="skyblue")


# 객체 생성
root=tk.Tk()
root.title("문제3")
canvas=tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=6)

# 값 저장 (라디오버튼, 라벨과 연결)
var=tk.StringVar(value="rect")
info=tk.StringVar(value="도형을 선택하고 그리기를 누르세오.")
tk.Label(root, textvariable=info).pack()

# 라디오버튼 프레임
f=tk.Frame(root)
f.pack(pady=6, anchor="center")

# 라디오버튼 생성
tk.Radiobutton(f, text="사각형", value="rect", variable=var).pack(side="left", padx=5)
tk.Radiobutton(f, text="원", value="circle", variable=var).pack(side="left", padx=5)

# 도형 그리기 함수 정의
def draw_shape():
    canvas.delete("all")
    if var.get()=="rect":
        s=Rectangle(50, 50, 100, 60)
    else:
        s=Circle(150, 110, 40)
    s.draw(canvas)
    info.set(f"면적={s.area():.2f}, 둘레={s.perimeter():.2f}")

# 버튼 배치
tk.Button(root, text="그리기", command=draw_shape).pack(pady=6)

root.mainloop()
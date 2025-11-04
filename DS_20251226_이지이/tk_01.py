from tkinter import *

class Book:
    def __init__(self, title, author, borrowed=False):
        self.title=title
        self.author=author
        self.borrowed=borrowed
    
    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            return f"{self.title}이(가) 대출되었습니다."
        return f"{self.title}은(는) 이미 대출 중입니다."

    def return_book(self):
        if self.borrowed:
            self.borrowed=False
            return f"{self.title}이(가) 반납되었습니다."
        return f"{self.title}은(는) 대출되지 않은 상태입니다."


def borrow_book():
    title=entry_title.get()
    author=entry_author.get()
    global book
    if not title or not author:
        label_result.config(text="제목과 저자를 모두 입력하세요.")
        return
    book=Book(title, author)
    msg=book.borrow() 
    label_result.config(text=msg, fg="blue")

def return_book():
    try:
        msg=book.return_book()
        label_result.config(text=msg, fg="green")
    except NameError:
        label_result.config(text="먼저 도서를 대출하세요.", fg="red")

root=Tk()
root.title=("도서 대출 관리 프로그램")
root.geometry("300x200")

Label(root, text="도서 대출 관리 시스템").pack()


Label(root, text="제목:").pack()
entry_title=Entry(root)
entry_title.pack()

Label(root, text="저자").pack()
entry_author=Entry(root)
entry_author.pack()

f=Frame(root)
f.pack(pady=20)

Button(f, text="대출", width=10, command=borrow_book).pack(side="left", padx=10, pady=10)
Button(f, text="반납", width=10, command=return_book).pack(side="left", padx=10, pady=10)

label_result=Label(root, text="")
label_result.pack()

root.mainloop()
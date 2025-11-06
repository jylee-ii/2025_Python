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

borrowed_books=[]

def update_borrowed_list():
    if borrowed_books:
        bookds_str=",".join([f"{self.title}({self.author})" for b in borrowed_books])
    else:
        return f"현재 대출 중인 도서가 없습니다."
    
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

    for b in borrowed_books:
        if b.title==title and b.author==author:
            label_result.config(text=f"{title}은(는) 이미 대출 중입니다.", fg="red")
            return
    book=Book(title, author)
    msg=book.borrow()
    borrowed_books.append(book)
    label_result.config(text=msg, fg="blue")
    update_borrowed_list()

def return_book():
    title=entry_title.get()
    author=entry_author.get()
    if not title or not author:
        label_result.config(text="제목과 저자를 모두 입력하세요.",fg='red')
        
    for b in borrowed_books:
        if b.title==title and b.author==author:
            borrowed_books.remove(b)
            label_result.config(text=f"{title}이(가) 반납되었습니다.",fg="green")
            update_borrowd_list()
            return
    
    label_result.config(text=f"{title}은(는) 대출 목록에 없습니다.",fg="green")
    

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

class Book:
    def __init__(self, title, author, borrowed=False):
        self.title=title
        self.author=author
        self.borrowed=borrowed
    
    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            print(f"{self.title}이(가) 대출되었습니다.")
        print(f"{self.title}은(는) 이미 대출 중입니다.")
            

    def return_book(self):
        print(f"{self.title}이(가) 반납되었습니다.")
        self.borrowed=False


b1=Book("파이썬 프로그래밍","홍길동")
b1.borrow()
b1.return_book()

import tkinter as tk
from tkinter import messagebox

# ---------- 모델 (상속/오버라이딩/다형성) ----------
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)
    def total_price(self, qty):
        return self.price * qty
    def __str__(self):
        return f"메뉴 : {self.name}, 단가 : {self.price:,}원"

class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = int(delivery_fee)
    def total_price(self, qty):  # 오버라이딩
        return super().total_price(qty) + self.delivery_fee
    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price:,}원, 배달비: {self.delivery_fee:,}원"

class Order:
    def __init__(self):
        self.items = []
    def add(self, food, qty):
        self.items.append((food, qty))
    def clear(self):
        self.items.clear()
    def total(self):
        return sum(f.total_price(q) for f, q in self.items)
    def summary_lines(self):
        lines = [f"{f.name} x {q} → {f.total_price(q):,}원" for f, q in self.items]
        lines += ["-"*28, f"합계: {self.total():,}원"]
        return "\n".join(lines)

# ---------- GUI ----------
def add_to_cart():
    sel = menu_list.curselection()
    if not sel:
        messagebox.showwarning("안내", "메뉴를 선택하세요.")
        return
    qty = max(1, int(qty_var.get()))
    order.add(menu_items[sel[0]], qty)
    cart_list.insert("end", f"{menu_items[sel[0]].name} x {qty}")
    total_label.config(text=f"합계: {order.total():,}원")

def place_order(): #알림버튼
    if not order.items:
        messagebox.showinfo("알림", "장바구니가 비어 있습니다.")
        return
    messagebox.showinfo("영수증", order.summary_lines())

def clear_cart(): #비우기버튼
    if not order.items:
        messagebox.showinfo("알림", "이미 장바구니가 비어 있습니다.")
        return
    if messagebox.askyesno("확인", "장바구니를 모두 비우시겠습니까?"):
        order.clear()
        cart_list.delete(0, "end")
        total_label.config(text="합계: 0원")

root = tk.Tk()
root.title("주문·배달 시스템")
root.geometry("600x380")

order = Order()
menu_items = [
    Food("김밥", 3000),
    Food("라면", 4000),
    Food("떡볶이", 5000),
    DeliveryFood("치킨", 18000, 3000),
    DeliveryFood("피자", 20000, 3000),
]

# 왼쪽 오른쪽 좌우 나누기
left = tk.Frame(root, padx=8, pady=8); left.pack(side="left", fill="both", expand=True)
right = tk.Frame(root, padx=8, pady=8); right.pack(side="right", fill="both", expand=True)

# 왼쪽: 메뉴목록, 수량, 장바구니 담기
tk.Label(left, text="메뉴 목록").pack(anchor="w")
menu_list = tk.Listbox(left, height=10); menu_list.pack(fill="both", expand=True)
for m in menu_items:
    menu_list.insert("end", str(m))     # __str__()으로 표시

ctrl = tk.Frame(left) #하위버튼만들기
ctrl.pack(pady=6) #여백
tk.Label(ctrl, text="수량").pack(side="left")
qty_var = tk.IntVar(value=1)

tk.Spinbox(ctrl, from_=1, to=20, width=5, textvariable=qty_var, justify="center").pack(side="left", padx=6) #수량

tk.Button(ctrl, text="장바구니 담기", command=add_to_cart).pack(side="left")

# 오른쪽: 장바구니, 합계, 주문, 전체비우기
tk.Label(right, text="장바구니").pack(anchor="w")
cart_list = tk.Listbox(right, height=10); cart_list.pack(fill="both", expand=True)

bottom = tk.Frame(right); bottom.pack(fill="x", pady=8)
total_label = tk.Label(bottom, text="합계: 0원"); total_label.pack(side="left")
btn_frame = tk.Frame(bottom)
btn_frame.pack(side="right")
tk.Button(btn_frame, text="전체 비우기", command=clear_cart).pack(side="right", padx=5)
tk.Button(btn_frame, text="주문하기", command=place_order).pack(side="right")
root.mainloop()
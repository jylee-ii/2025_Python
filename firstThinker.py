import tkinter as tk

root=tk.Tk()
root.title("TKinter 예제")
root.geometry("200x100")

label=tk.Label(root, text="Hello, TKinter!")
label.pack(pady=20)

root.mainloop()
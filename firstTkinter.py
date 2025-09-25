import tkinter as tk

root=tk.TK()
root.title("TKinter 예제")
root.geoetry("200*100")

label=tk.Label(root, text="Hello, TKinter!")
label.pack(pady=20)

root.mainloop()
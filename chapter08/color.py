from tkinter import *

root=Tk()

button=Button(root, text="클릭하세요")
button.pack()
button["fg"]="#ff0000"
button["bg"]="#00ff00"

root.mainloop()
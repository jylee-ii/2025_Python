import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    x = float(x_entry.get())
    y = float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker='o', linestyle='-')
    canvas.draw()
    
#어플리케이션 초기 설정
root = tk.Tk()
root.title("Dynamic Line Graph ")
x_data=[]
y_data=[] #x좌표 데이터 저장할리스트 
x_label=tk.Label(root, text="Enter x coordinate:")
x_label.pack() 
x_entry=tk.Entry(root)
x_entry.pack()

y_label=tk.Label(root, text="Enter y oordinate:")
y_label.pack()
y_entry=tk.Entry(root)
y_entry.pack()
plot_button = tk.Button(root, text="Plot", command=plot_graph)
plot_button.pack() 
 
#Matplotlib Figure 생성
fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack() 

#어플리케이션 실행
root.mainloop()
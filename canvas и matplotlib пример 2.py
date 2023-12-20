
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from random import choice


x_list = [0]
y_list = [0]

def fill_arrs():
    counter = 10000
    while counter > 0:
        x_direction = choice([1, -1])
        x_dist = choice([1, 2, 3, 4])
        x_step = x_direction * x_dist
        x = x_list[-1] + x_step
        x_list.append(x)

        y_direction = choice([1, -1])
        y_dist = choice([1, 2, 3, 4])
        y_step = y_direction * y_dist
        y = y_list[-1] + y_step
        y_list.append(y)

        counter -= 1

def generate_scatter_chart(uebergebene_daten=(10, 10, 10, 10)):
    global canvas1
    if canvas1:
        canvas1.get_tk_widget().destroy()
    datenplot = uebergebene_daten
    fig = Figure(figsize=(10, 4), dpi=100)
    ax = fig.add_subplot(111) 

    fill_arrs()   
    ax.scatter(x_list, y_list, s = 1)    

    canvas1 = FigureCanvasTkAgg(fig, master = window)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=TOP, fill=NONE, expand=0)
    window.after(200, None)

def close_scatter_chart():
    global canvas1
    if canvas1:
        canvas1.get_tk_widget().destroy()    
    

window = Tk() 

canvas1 = None

window.title('Plotting in Tkinter') 
window.geometry("700x500") 

btn = Button(
    master = window, 
    text = 'Generate scatter chart', 
    command = generate_scatter_chart, 
    padx = 5, pady = 5
)
btn.pack()

btn2 = Button(
    master = window, 
    text = 'Close scatter chart', 
    command = close_scatter_chart, 
    padx = 5, pady = 5
)
btn2.pack()

window.mainloop()


# form:
# https://ru.stackoverflow.com/questions/1236316/%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BA%D0%BD%D0%B0%D0%BC%D0%B8-tkinter-%D0%92%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA-matplotlib-%D0%B2-%D0%BE%D0%BA%D0%BD%D0%BE-tkinter
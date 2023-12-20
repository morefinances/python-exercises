from tkinter import Tk, Canvas, Frame, BOTH
 
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
        # canvas.create_line(15, 25, 200, 25)
        canvas.create_line(200, 20, 200, 330, dash=(4, 2))
        # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.create_rectangle(
            30, 20, 130, 120,
            outline="#000000", fill="white"
        )
        
        canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    ex = Example()
    root.geometry("500x350+300+300")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
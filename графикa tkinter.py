from tkinter import *
 

root = Tk()

fullheght = 774
fullwidth = 1278
screenborder = 20 

c = Canvas(root, width = fullwidth, height = fullheght, bg='white')
c.pack()
 
c.create_rectangle(screenborder, screenborder, 
                   fullwidth - screenborder, fullheght - screenborder, 
                   outline="#000000")

for ii in range(6):
    if ii > 0:
        tt = 1
    else:
        tt = 0
    c.create_line(screenborder - 10,  fullheght - ii*140 - screenborder - tt,
                  screenborder, fullheght - ii*140 - screenborder - tt)

for xx in range(9):
    if xx > 0:
        tt = 1
    else:
        tt = 0
    c.create_line(screenborder + xx*140 + tt, fullheght - 20,
                  screenborder + xx*140 + tt, fullheght - 8)
    c.create_line(screenborder + xx*140 + tt, 8,
                  screenborder + xx*140 + tt, 20)

# c.create_line(200, 20, 200, 330, dash=(4, 2))
for u in range(52):
    for i in range(88):
        # print(i)
        c.create_rectangle(
            screenborder + 5 + i*14, screenborder + 5 + u*14, 
            screenborder + 15 + i*14, 35 + u*14,
            outline="#000000", fill="white"
        )


root.mainloop()




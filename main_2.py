from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Weight Converter")
root.geometry("300x400")

label_1 = Label(root,text="Weight in KG:",font = font.Font(size = 20))
label_1.pack(pady = 10)

entry_1 = Entry(root)
entry_1.pack()

frame = Frame(root)
frame.pack()

label_2 = Label(frame,text="Grams:",font=font.Font(size=15))
label_2.grid(row=1,column=0,pady=10)

label_3 = Label(frame,font=font.Font(size=15))
label_3.grid(row=1,column=1)



root.mainloop()
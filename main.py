from tkinter import *
import tkinter.font as font 

root = Tk()
root.title("Temperture Converter")
root.geometry("500x250")

def convert():
    celsius = entry.get()
    if(celsius.replace(".","").isnumeric()):
        label_3.grid_forget()
        farh = (float(celsius)* 9/5)+32
        label_4.config(text="Temperture in fahrenheit:"+str(farh))
    else:
        label_3.grid(row=1,column=1,pady=5)


label_1 = Label(root,text="Celsius --> Fahrenheit",font = font.Font(size = 20),fg = "grey")
label_1.pack(pady=20)

frame = Frame(root)
frame.pack(pady=10)

label_2 = Label(frame,text="Enter Temperture in Celsius:")
label_2.grid(row=0,column=0,pady=5)

entry = Entry(frame)
entry.grid(row=0,column=1,pady=5)

label_3 = Label(frame,text="Please entry a vaild input...",fg="red",font= font.Font(size=10))

label_4 = Label(frame)
label_4.grid(row=2,column=0,pady=5)

btn = Button(frame,text="Convert",bg="light green",fg="black",command= convert)
btn.grid(row=3,column=0,pady=5)




root.mainloop()
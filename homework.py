from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Currency Converter")
root.geometry("500x250")

def convert():
    usd = entry.get()
    if(usd.replace(".","").isnumeric()):
        label_3.grid_forget()
        inr = float(usd) * 94.5
        text.delete("1.0",END)
        text.insert(END,"Amount in INR:"+str(inr))
    else:
        label_3.grid(row=1,column=1,pady=5)


label_1 = Label(root,text="USD --> INR",font=font.Font(size=20),fg="grey")
label_1.pack(pady=20)

frame = Frame(root)
frame.pack(pady=10)

label_2 = Label(frame,text="Enter Amount in USD:")
label_2.grid(row=0,column=0,pady=5)

entry = Entry(frame)
entry.grid(row=0,column=1,pady=5)

label_3 = Label(frame,text="Please entry a valid input...",fg="red",font=font.Font(size=10))

text = Text(frame,height=1,width=20)
text.grid(row=2,column=0,pady=5)

btn = Button(frame,text="Convert",bg="light green",fg="black",command=convert)
btn.grid(row=3,column=0,pady=5)

root.mainloop()

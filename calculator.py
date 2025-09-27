from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("500x660")
window.configure(bg="BLACK")
# Entry box
e = Entry(window, width=63, borderwidth=10, font=("Arial", 9, "bold"))
e.place(x=15, y=15)
#function of showing a number or operator in entry box
def click(value):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(value))
#clear the number or operator in entry box
def cls():
    e.delete(0, END)
#backspace
def backspace():
    current = e.get()
    if current:
        e.delete(len(current) - 1, END)
#this function is for operation
def equal():
    try:
        result = eval(e.get())#eval automatically add,div etcby given expression
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")
Button(window, text="C", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=cls).place(x=20, y=60)
Button(window, text="<-", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=backspace).place(x=140, y=60)
Button(window, text="/", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('/')).place(x=260, y=60)
Button(window, text="*", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('*')).place(x=380, y=60)
Button(window, text="1", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('1')).place(x=20, y=120)
Button(window, text="2", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('2')).place(x=140, y=120)
Button(window, text="3", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('3')).place(x=260, y=120)
Button(window, text="-", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('-')).place(x=380, y=120)
Button(window, text="4", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('4')).place(x=20, y=180)
Button(window, text="5", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('5')).place(x=140, y=180)
Button(window, text="6", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('6')).place(x=260, y=180)
Button(window, text="+", width=12, height=6, bg="GRAY", fg="black", relief="ridge", command=lambda: click('+')).place(x=380, y=180)
Button(window, text="7", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('7')).place(x=20, y=240)
Button(window, text="8", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('8')).place(x=140, y=240)
Button(window, text="9", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('9')).place(x=260, y=240)
Button(window, text=".", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('.')).place(x=20, y=300)
Button(window, text="0", width=12, height=2, bg="GRAY", fg="black", relief="ridge", command=lambda: click('0')).place(x=140, y=300)
Button(window, text="=", width=29, height=2, bg="GRAY", fg="black", relief="ridge", command=equal).place(x=260, y=300)
window.mainloop()

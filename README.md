# Python-Assignment-6
CALCULATOR USING TKINTER
from tkinter import * is for all
create a gui interaction by window=Tk()
create title calculator and layout using window.geometry 500x600 and background colour black
create entry box by variable Entry window width of the entry box borderwidth fonts and place it in the layout
create a function for showing a number or a operator in the entry box by def function name click that takes one parameter value
current is a variable that stores values by e.get()
e.delet(0,END) clear the entry box
e.insert(0,current+str(valus)) 0 is the index of the entry box and current stores the values which user entry in entry box and add the value which is converted in string
again created a function with name cls for clearing all element present in entry box
again created a function with name of backspace for deleting one by one element
again create a funtion with name equal for calculating the opration
i have used try becasue The try block is used to attempt to evaluate the expression entered in the Entry box using Python’s built-in eval() function this expression could include numbers and operators like +, -, *, /
create button by variable b= builtinfunctin Button window text width border width and height bg colour fg colour relief add 3d or 2d shape for button command for which button you are giviing ex for deleting one number in entry box give command and function name backspace
and create button for other for number button the command will be lambda:click 1 for text1
thank you

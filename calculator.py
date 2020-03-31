from tkinter import *
import parser
import tkinter.messagebox

root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

'''
function to insert numbers in the field

'''
i=0
def get_num(num):
    global i
    display.insert(i, num)
    i+=1


'''
function to calculate the expression
'''

def calculate():
    entire_str = display.get()
    try:
        result = eval(parser.expr(entire_str).compile())
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        tkinter.messagebox.showinfo("Error", "UNKOWN ERROR!!")

'''
functions to display operators
'''
def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length


'''
function to calculate factorial
'''
def fact():
    fact = 1
    try:
        num = int(display.get())
        clear_all()
        if num<0:
            tkinter.messagebox.showinfo("negative number", "sorry no factorial for negative numbers")
        elif num == 0:
            display.insert(0, fact)
        else:
            for i in range(1, num+1):
                fact *= i
            display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "ERROR!!")


'''
function to clear the inputs
'''

def clear_all():
    display.delete(0, END)



'''
function to delete the single character
'''    
def undo():
    entire_str = display.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0, "Error!!")


#buttons added
Button(root, text="1", command= lambda : get_num(1)).grid(row=4, column=0)
Button(root, text="2", command= lambda : get_num(2)).grid(row=4, column=1)
Button(root, text="3", command= lambda : get_num(3)).grid(row=4, column=2)
Button(root, text="4", command= lambda : get_num(4)).grid(row=3, column=0)
Button(root, text="5", command= lambda : get_num(5)).grid(row=3, column=1)
Button(root, text="6", command= lambda : get_num(6)).grid(row=3, column=2)
Button(root, text="7", command= lambda : get_num(7)).grid(row=2, column=0)
Button(root, text="8", command= lambda : get_num(8)).grid(row=2, column=1)
Button(root, text="9", command= lambda : get_num(9)).grid(row=2, column=2)

Button(root, text="AC", command= lambda : clear_all()).grid(row=5, column=0)
Button(root, text="0", command= lambda : get_num(0)).grid(row=5, column=1)
Button(root, text="=", command= lambda : calculate()).grid(row=5, column=2)

Button(root, text="+", command= lambda : get_operator("+")).grid(row=2, column=3)
Button(root, text="-", command= lambda : get_operator("-")).grid(row=3, column=3)
Button(root, text="*", command= lambda : get_operator("*")).grid(row=4, column=3)
Button(root, text="/", command= lambda : get_operator("/")).grid(row=5, column=3)

Button(root, text="pi", command= lambda : get_operator("3.14")).grid(row=2, column=4)
Button(root, text="%", command= lambda : get_operator("%")).grid(row=3, column=4)
Button(root, text="(", command= lambda : get_operator("(")).grid(row=4, column=4)
Button(root, text="exp", command= lambda : get_operator("**")).grid(row=5, column=4)

Button(root, text="del", command= lambda : undo()).grid(row=2, column=5)
Button(root, text="x!", command= lambda : fact()).grid(row=3, column=5)
Button(root, text=")", command= lambda : get_operator(")")).grid(row=4, column=5)
Button(root, text="^2", command= lambda : get_operator("^2")).grid(row=5, column=5)

root.mainloop()
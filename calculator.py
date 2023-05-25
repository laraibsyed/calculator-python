from tkinter import *  # import tkinter
import math  # import math for some calculations
from time import sleep, perf_counter  # importing sleep and perf_counter from time
from threading import Thread  # importing Thread from threading
root = Tk()  # displays root window and manages tkinter application
root.geometry("650x400+300+300")  # decides size and position of the screen layout
root.title("CST1500 Python Coursework - Calculator")  # title of the tkinter window

switch = None  # defines a null value, is a datatype on its own


def one():  # defines the function for the number 1
    if disp.get() == '0':  # if the value entered by the user is 0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '1')  # puts the value into pos


def two():  # defines the function for the number 2
    if disp.get() == '0':  # if the value entered by the user is 0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '2')  # puts the value into pos


def three():  # defines the function for the number 3
    if disp.get() == '0':  # if the value entered by the user is 0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '3')  # puts the value into pos


def four():  # defines the function for the number 4
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '4')  # puts the value into pos


def five():  # defines the function for the number 5
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '5')  # puts the value into pos


def six():  # defines the function for the number 6
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '6')  # puts the value into pos


def seven():  # defines the function for the number 7
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '7')  # puts the value into pos


def eight():  # defines the function for the number 8
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '8')  # puts the value into pos


def nine():  # defines the function for the number 9
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '9')  # puts the value into pos


def zero():  # defines the function for the number 0
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '0')  # puts the value into pos


def key_event(*args):  # contains information about key press and release events
    if disp.get() == '0':  # if the value entered by the user is  0
        disp.delete(0, END)  # the program ignores the 0


def addition():  # defines the function for addition
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '+')  # puts the value into pos


def subtraction():  # defines the function for subtraction
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '-')  # puts the value into pos


def multiplication():  # defines the function for multiplication
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '*')  # puts the value into pos


def division():  # defines the function for division
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '/')  # puts the value into pos


def clear(*args):  # defines the function for clearing the screen
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, '0')  # puts the value into pos


def sin():  # defines the function for sin
    ans = float(disp.get())  # value is given as a float (decimal)
    if switch is True:  # checks if the statement is true
        ans = math.sin(math.radians(ans))  # converts degree value into radians
    else:
        ans = math.sin(ans)  # the value is saved into a variable named ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def cos():  # defines the function for cosine
    ans = float(disp.get())  # the value is saved into a variable named ans
    if switch is True:  # checks if the statement is true
        ans = math.cos(math.radians(ans))  # converts degree value into radians
    else:
        ans = math.cos(ans)  # converts degree value into degrees and saves it into ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def tan():  # defines the function for tan
    ans = float(disp.get())  # the value is saved into a variable named ans
    if switch is True:  # checks if the statement is true
        ans = math.tan(math.radians(ans))  # converts degree value into radians
    else:
        ans = math.tan(ans)  # the value is saved into a variable named ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def inverse_sin():  # defines the function for inverse of sin
    ans = float(disp.get())  # the value is saved into a variable named ans
    if switch is True:  # checks if the statement is true
        ans = math.degrees(math.asin(ans))
    else:
        ans = math.asin(ans)  # converts degree value into radians
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def inverse_cos():  # defines the function for inverse of cosine
    ans = float(disp.get())  # the value is saved into a variable named ans
    if switch is True:  # checks if the statement is true
        ans = math.degrees(math.acos(ans))
    else:
        ans = math.acos(ans)  # converts degree value into radians
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def inverse_tan():  # defines the function for inverse of tan
    ans = float(disp.get())  # the value is saved into a variable named ans
    if switch is True:  # checks if the statement is true
        ans = math.degrees(math.atan(ans))
    else:
        ans = math.atan(ans)  # converts degree value into radians
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def power():  # defines the function for powers
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '**')  # puts the value into pos


def rounding():  # defines the function for rounding a number
    ans = float(disp.get())  # the value is saved into a variable named ans
    ans = round(ans)  # the rounded value is updated into the variable ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def log():  # defines the function for logarithms
    ans = float(disp.get())  # the value is saved into a variable named ans
    ans = math.log10(ans)  # the calculated value is updated into the variable ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def factorial():  # defines the function for factorials
    ans = float(disp.get())  # the value is saved into a variable named ans
    ans = math.factorial(ans)  # the calculated value is updated into the variable ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def square_root():  # defines the function for square root
    ans = float(disp.get())  # the value is saved into a variable named ans
    ans = math.sqrt(ans)  # the calculated value is updated into the variable ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def decimal_point():  # defines the function for the decimal point
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '.')  # puts the value into pos


def pi():  # defines the function for pi
    if disp.get() == '0':  # if the value entered by the user is 0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, str(math.pi))  # puts the value into pos


def e():  # defines the function for e
    if disp.get() == '0':  # if the value entered by the user is 0
        disp.delete(0, END)  # the program ignores the 0
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, str(math.e))  # puts the value into pos


def opening_bracket():  # defines the function for
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '(')  # puts the value into pos


def closing_bracket():  # defines the function for
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, ')')  # puts the value into pos


def delete(*args):  # defines the function for backspace
    pos = len(disp.get())  # the value is saved into a variable named pos
    display = str(disp.get())  # the value is turned into a string and saved into a variable named display
    if display == '':  # if the value entered is empty
        disp.insert(0, '0')  # puts the value into pos
    elif display == ' ':  # if the value entered is empty
        disp.insert(0, '0')  # puts the value into pos
    elif display == '0':  # if the value entered is 0
        pass  # skip
    else:
        disp.delete(0, END)  # the program ignores the 0
        disp.insert(0, display[0:pos - 1])  # puts the value into pos


def numberType():  # defines the function for whether the user wants RAD or DEG
    global switch  # allows you to modify the variable outside the current scope
    if switch is None:  # if switch is none
        switch = True  # checks if switch is true
        conv_btn['text'] = "Deg"  # the conv_btn text shows as "Deg"
    else:
        switch = None  # else if switch is not true
        conv_btn['text'] = "Rad"  # the conv_btn text shows as "Rad"


def ln():  # defines the function for ln
    ans = float(disp.get())  # the value is saved into a variable named ans
    ans = math.log(ans)  # the calculated value is updated into the variable ans
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, str(ans))  # puts the value into pos


def percentage():  # defines the function for percentages
    pos = len(disp.get())  # the value is saved into a variable named pos
    disp.insert(pos, '%')  # puts the value into pos


def equal():  # defines the function for equals
    ans = disp.get()  # value entered by user is stored in the variable ans
    ans = eval(ans)  # calculated value is shown when user clicks =
    disp.delete(0, END)  # the program ignores the 0
    disp.insert(0, ans)  # puts the value into pos


def task():  # defines the function for running the program
    print('Starting a task...')  # prints starting a task
    sleep(1)  # sleeps for 1 second
    print('Done')  # prints "done"


start_time = perf_counter()  # starts the function

t1 = Thread(target=task)  # creating a new thread

t1.start()  # starting the thread

t1.join()  # waiting for the thread to complete

end_time = perf_counter()  # ends the function and returns the float value of time in seconds

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')  # printing the time it took to run the GUI

disp = Entry(root, font="Ubuntu 20", fg="black", bg="#344377", bd=0, justify=RIGHT, insertbackground="#344377",
             cursor="arrow")  # font and background color for when the user enters something
disp.bind("<Return>", equal)
disp.bind("<Escape>", clear)  # key event to clear the calculation
disp.bind("<Key-1>", key_event)  # key event to press 1 on your keyboard
disp.bind("<Key-2>", key_event)  # key event to press 2 on your keyboard
disp.bind("<Key-3>", key_event)  # key event to press 3 on your keyboard
disp.bind("<Key-4>", key_event)  # key event to press 4 on your keyboard
disp.bind("<Key-5>", key_event)  # key event to press 5 on your keyboard
disp.bind("<Key-6>", key_event)  # key event to press 6 on your keyboard
disp.bind("<Key-7>", key_event)  # key event to press 7 on your keyboard
disp.bind("<Key-8>", key_event)  # key event to press 8 on your keyboard
disp.bind("<Key-9>", key_event)  # key event to press 9 on your keyboard
disp.bind("<Key-0>", key_event)  # key event to press 0 on your keyboard
disp.bind("<Key-.>", key_event)  # key event to press . on your keyboard
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# first row of buttons

btnrow1 = Frame(root, bg="#000000")  # groups and organizes widgets and background color
btnrow1.pack(expand=TRUE, fill=BOTH)  # calls back the button

factorial_btn = Button(btnrow1, text=" x! ", font="Ubuntu 18", command=factorial, fg="black",
                       bg="#333333")  # the way the button text is displayed and its font size and color
factorial_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

conv_btn = Button(btnrow1, text="Rad", font="Ubuntu 12 bold", command=numberType, fg="black",
                  bg="#333333")  # the way the button text is displayed and its font size and color
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

sqr_root_btn = Button(btnrow1, text=" √x ", font="Ubuntu 18", command=square_root, fg="black",
                      bg="#333333")  # the way the button text is displayed and its font size and color
sqr_root_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_clear = Button(btnrow1, text="C", font="Ubuntu 23", command=clear, fg="red",
                   bg="#333333")  # the way the button text is displayed and its font size and color
btn_clear.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

opening_bracket_btn = Button(btnrow1, text=" ( ", font="Ubuntu 21", command=opening_bracket, fg="green",
                             bg="#333333")  # the way the button text is displayed and its font size and color
opening_bracket_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

closing_bracket_btn = Button(btnrow1, text=" ) ", font="Ubuntu 21", command=closing_bracket, fg="green",
                             bg="#333333")  # the way the button text is displayed and its font size and color
closing_bracket_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_division = Button(btnrow1, text="/", font="Ubuntu 23", command=division, fg="green",
                      bg="#333333")  # the way the button text is displayed and its font size and color
btn_division.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

# second row of buttons

btnrow2 = Frame(root)  # groups and organizes widgets
btnrow2.pack(expand=TRUE, fill=BOTH)  # calls back the button

pow_btn = Button(btnrow2, text="x^y", font="Ubuntu 17", command=power, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

sin_btn = Button(btnrow2, text="sin", font="Ubuntu 18", command=sin, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

cos_btn = Button(btnrow2, text="cos", font="Ubuntu 18", command=cos, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

tan_btn = Button(btnrow2, text="tan", font="Ubuntu 18", command=tan, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn7 = Button(btnrow2, text="7", font="Ubuntu 23", command=seven, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn8 = Button(btnrow2, text="8", font="Ubuntu 23", command=eight, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn9 = Button(btnrow2, text="9", font="Ubuntu 23", command=nine, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_multiply = Button(btnrow2, text="x", font="Ubuntu 23", command=multiplication, fg="green",
                      bg="#333333")  # the way the button text is displayed and its font size and color
btn_multiply.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

# third row of buttons

btnrow3 = Frame(root)  # groups and organizes widgets
btnrow3.pack(expand=TRUE, fill=BOTH)  # calls back the button

sin_inverse_btn = Button(btnrow3, text="sin−1", font="Ubuntu 11 bold", command=inverse_sin, fg="black",
                  bg="#333333")  # the way the button text is displayed and its font size and color
sin_inverse_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

cos_inverse_btn = Button(btnrow3, text="cos-1", font="Ubuntu 11 bold", command=inverse_cos, fg="black",
                  bg="#333333")  # the way the button text is displayed and its font size and color
cos_inverse_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

tan_inverse_btn = Button(btnrow3, text="tan-1", font="Ubuntu 11 bold", command=inverse_tan, fg="black",
                  bg="#333333")  # the way the button text is displayed and its font size and color
tan_inverse_btn .pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn4 = Button(btnrow3, text="4", font="Ubuntu 23", command=four, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn5 = Button(btnrow3, text="5", font="Ubuntu 23", command=five, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn6 = Button(btnrow3, text="6", font="Ubuntu 23", command=six, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_minus = Button(btnrow3, text="-", font="Ubuntu 23", command=subtraction, fg="green",
                   bg="#333333")  # the way the button text is displayed and its font size and color
btn_minus.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

# fourth row of buttons

btnrow4 = Frame(root)  # groups and organizes widgets
btnrow4.pack(expand=TRUE, fill=BOTH)  # calls back the button

round_btn = Button(btnrow4, text="round", font="Ubuntu 10 bold", command=rounding, fg="black",
                   bg="#333333")  # the way the button text is displayed and its font size and color
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

ln_btn = Button(btnrow4, text="ln", font="Ubuntu 18", command=ln, fg="black",
                bg="#333333")  # the way the button text is displayed and its font size and color
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

logarithm_btn = Button(btnrow4, text="log", font="Ubuntu 17", command=log, fg="black",
                       bg="#333333")  # the way the button text is displayed and its font size and color
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn1 = Button(btnrow4, text="1", font="Ubuntu 23", command=one, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn2 = Button(btnrow4, text="2", font="Ubuntu 23", command=two, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn3 = Button(btnrow4, text="3", font="Ubuntu 23", command=three, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_add = Button(btnrow4, text="+", font="Ubuntu 23", command=addition, fg="green",
                 bg="#333333")  # the way the button text is displayed and its font size and color
btn_add.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

# fifth row of buttons

btnrow5 = Frame(root)  # groups and organizes widgets
btnrow5.pack(expand=TRUE, fill=BOTH)  # calls back the button

percent_btn = Button(btnrow5, text="%", font="Ubuntu 21", command=percentage, fg="green",
                     bg="#333333")  # the way the button text is displayed and its font size and color
percent_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

e_btn = Button(btnrow5, text="e", font="Ubuntu 18", command=e, fg="black",
               bg="#333333")  # the way the button text is displayed and its font size and color
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

pi_btn = Button(btnrow5, text="π", font="Ubuntu 18", command=pi, fg="black",
                bg="#333333")  # the way the button text is displayed and its font size and color
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

del_btn = Button(btnrow5, text="⌫", font="Ubuntu 20", command=delete, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn0 = Button(btnrow5, text="0", font="Ubuntu 23", command=zero, fg="black",
              bg="#333333")  # the way the button text is displayed and its font size and color
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

dot_btn = Button(btnrow5, text=" • ", font="Ubuntu 21", command=decimal_point, fg="black",
                 bg="#333333")  # the way the button text is displayed and its font size and color
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button

btn_equal = Button(btnrow5, text="=", font="Ubuntu 23", command=equal, fg="green",
                   bg="#333333")  # the way the button text is displayed and its font size and color
btn_equal.pack(side=LEFT, expand=TRUE, fill=BOTH)  # calls back the button
root.mainloop()  # runs the tkinter events

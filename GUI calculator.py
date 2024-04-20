import tkinter as tk
calculation = ""

def calculate (ele):
    global calculation 
    calculation += str(ele)
    tfield.delete(1.0 , "end")
    tfield.insert(1.0 , calculation)
    
def evaluate():
    global calculation 
    try:
        
        calculation = str(eval(calculation))
        tfield.delete(1.0 , "end")
        tfield.insert(1.0 , calculation)
    except:
        tfield.insert(1.0 , "Error") 

def clear():
    global calculation 
    calculation = ""
    tfield.delete(1.0 , "end")
    



window = tk.Tk()
# label = tk.Label(window , text="Caculator")
# label.pack()
window.geometry("300x275")
tfield = tk.Text(window, height=2 , width=16 , font=("Arial" , 24))
tfield.grid(columnspan=5)

btn1 = tk.Button(window , text="1" , command=lambda : calculate(1) , width=5 , font=("Arial" , 14))
btn1.grid(row = 2 , column=1)
btn2 = tk.Button(window , text="2" , command=lambda : calculate(2) , width=5 , font=("Arial" , 14))
btn2.grid(row = 2 , column=2)
btn3 = tk.Button(window , text="3" , command=lambda : calculate(3) , width=5 , font=("Arial" , 14))
btn3.grid(row = 2 , column=3)
btn4 = tk.Button(window , text="4" , command=lambda : calculate(4) , width=5 , font=("Arial" , 14))
btn4.grid(row = 3 , column=1)
btn5 = tk.Button(window , text="5" , command=lambda : calculate(5) , width=5 , font=("Arial" , 14))
btn5.grid(row = 3 , column=2)
btn6 = tk.Button(window , text="6" , command=lambda : calculate(6) , width=5 , font=("Arial" , 14))
btn6.grid(row = 3 , column=3)
btn7 = tk.Button(window , text="7" , command=lambda : calculate(7) , width=5 , font=("Arial" , 14))
btn7.grid(row = 4 , column=1)
btn8 = tk.Button(window , text="8" , command=lambda : calculate(8) , width=5 , font=("Arial" , 14))
btn8.grid(row = 4 , column=2)
btn9 = tk.Button(window , text="9" , command=lambda : calculate(9) , width=5 , font=("Arial" , 14))
btn9.grid(row = 4 , column=3)
btndec = tk.Button(window , text="." , command=lambda : calculate('.') , width=5 , font=("Arial" , 14))
btndec.grid(row = 5 , column=1)
btn0 = tk.Button(window , text="0" , command=lambda : calculate(0) , width=5 , font=("Arial" , 14))
btn0.grid(row = 5 , column=2)
btnc = tk.Button(window , text="C" , command= clear , width=5 , font=("Arial" , 14))
btnc.grid(row = 5 , column=3)
btnopen = tk.Button(window , text="(" , command=lambda : calculate('(') , width=5 , font=("Arial" , 14))
btnopen.grid(row = 6 , column=1)
btnclose = tk.Button(window , text=")" , command=lambda : calculate(')') , width=5 , font=("Arial" , 14))
btnclose.grid(row = 6 , column=2)
btnequal = tk.Button(window , text="=" , command= evaluate , width=11 , font=("Arial" , 14))
btnequal.grid(row = 6 , column=3 , columnspan=2)
btnadd = tk.Button(window , text="+" , command=lambda : calculate('+') , width=5 , font=("Arial" , 14))
btnadd.grid(row = 2 , column=4)
btnsub = tk.Button(window , text="-" , command=lambda : calculate('-') , width=5 , font=("Arial" , 14))
btnsub.grid(row = 3 , column=4)
btndiv = tk.Button(window , text="/" , command=lambda : calculate('/') , width=5 , font=("Arial" , 14))
btndiv.grid(row = 4 , column=4)
btnmul = tk.Button(window , text="*" , command=lambda : calculate('*') , width=5 , font=("Arial" , 14))
btnmul.grid(row = 5 , column=4)
window.mainloop()












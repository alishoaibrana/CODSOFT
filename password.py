import tkinter as tk
from random import randint 

def record_len():
    
    length = int(tf.get())
    # length = int(length)
    print(f"number of digits {length}")
    generate_pass(length)

def generate_pass(length):

    password = ""
    pw_entry.delete(0 , tk.END) 

    if length == 0:
        return
    for i in range(length):
        password += chr(randint(33,126))
    pw_entry.insert(0 , password)


def copy_pass():
    root.clipboard_clear()

    root.clipboard_append(pw_entry.get())

root = tk.Tk()
root.title("Password Generator")
root.geometry('500x400')
label1 = tk.Label(root , text="Enter the Length of Password" , font=('Arial' , 14),borderwidth=2)
label1.place(x=120 , y=100)
tf = tk.Entry(root,width=24,font=('Arial' , 12))
tf.place(x=120 , y=150)
pw_entry = tk.Entry(root , width=24 , font= ('Arial' , 12) , bg="systembuttonface" , bd=0)
pw_entry.place(x=120 , y=220)
button1 = tk.Button(root , text="Generate Password" , command=record_len , width=15 , padx=10)
button1.place(x=200 , y=300)
button2 = tk.Button(root , text="Copy Password" ,command=copy_pass , width=15 , padx=10)
button2.place(x=350 , y=300)

tk.mainloop()
import numpy as np
# import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox

# def press_enter_key(ev):
#     click_button()
#     messagebox.showinfo('cordinate value' , f"({ev.x}, {ev.y})")

def create_2d_array(row, col):
    return np.random.randint(1,101, size=(row, col))

def click_button(*args):
    try:
        r,c = map(int, en_row_column.get().split())
        matrix = create_2d_array(r,c)
        lbl_result.config(text=matrix)
    except ValueError as err:
        messagebox.showerror('Error!' , f"입력값없음. \n{err}")

window = tk.Tk()
window.title('numpy gui version v0.7')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy array")
en_row_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

#enter key bi
# en_row_column.bind("<Return>",press_enter_key)
en_row_column.bind("<Return>",click_button)
lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')

en_row_column.focus()

window.mainloop()

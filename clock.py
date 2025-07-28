import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")


root.geometry("300x100")
root.resizable(False, False)

clock_label = tk.Label(root, font=('times new roman', 60, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center')


def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  


update_time()


root.mainloop()

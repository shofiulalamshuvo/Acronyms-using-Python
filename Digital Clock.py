from tkinter import Label, Tk 
import time

app_window = Tk()
app_window.title("My Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font = ("Boulder", 70, 'bold')
background = "#ffffff"
foreground = "#000000"
border_width = 20

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def my_digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, my_digital_clock)

my_digital_clock()
app_window.mainloop()
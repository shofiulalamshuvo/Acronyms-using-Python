from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1000x1000+100+50")
        self.root.resizable(False, False)


        #Background Picture
        self.bg = ImageTk.PhotoImage(file= "background image.jpg") #add an image according to your wish
        self.bg_image = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)


        #login frame
        Frame_login = Frame(self.root, bg = "white")
        Frame_login.place(x = 330, y = 150, width = 500, height = 400)

        #Title & Subtitle
        title = Label(Frame_login, text = "Login Here", font = ("Impact", 35, "bold"), fg = "#6162FF", bg = "white").place(x = 90, y = 30)
        subtitle = Label(Frame_login, text = "Login Area for Staffs", font = ("Sans", 15, "bold"), fg = "#1d1d1d", bg = "white").place(x = 90, y = 100)

        #Username
        lbl_user = Label(Frame_login, text = "User Name", font = ("Sans Serif", 15, "bold"), fg = "grey", bg = "white").place(x = 90, y = 140)
        self.username = Entry(Frame_login, font=("Sans Serif", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width = 320, height = 35)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("Sans Serif", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Sans Serif", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forget = Button(Frame_login, text="Forgot Password?", bd = 0, cursor = "hand2", font=("Sans Serif", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        login = Button(Frame_login, command = self.check_function, cursor = "hand2", text="Login", bd=0, font=("Sans Serif", 15), bg="#6162FF", fg="white").place(x=90, y=320, width = 180, height = 40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields need to fullfil", parent = self.root)
        elif self.username.get() != "themteguy" or self.password.get() != "shuvo@@z2i008":
            messagebox.showerror("Error", "Invalid Username or Password", parent = self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")



root = Tk()
obj = Login(root)
root.mainloop()

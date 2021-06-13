#importing tkinter
from tkinter import *
root = Tk()
root.geometry("1000x1000") #height and weidth

#Declaraing that system gets your input and show a congratulations message
def getvals():
    print("Accepted your request")

#Heading Name
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

#Option Names
name = Label(root, text= "Name")
phone = Label(root, text= "Phone")
gender = Label(root, text= "Gender")
emergency = Label(root, text= "Emergency")
paymentmood = Label(root, text= "Payment Mood")

#Packing the Option Names
name.grid(row = 1, column= 2)
phone.grid(row = 2, column= 2)
gender.grid(row = 3, column= 2)
emergency.grid(row = 4, column= 2)
paymentmood.grid(row = 5, column= 2)

#Variable type declaration
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

#Entry Fields Creation
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymentmoodentry = Entry(root, textvariable = paymentmoodvalue)

#Packing the Entry Fields
nameentry.grid(row = 1, column= 3)
phoneentry.grid(row = 2, column= 3)
genderentry.grid(row = 3, column= 3)
emergencyentry.grid(row = 4, column= 3)
paymentmoodentry.grid(row = 5, column= 3)

#Checkbox Creation
checkbtn = Checkbutton(text = "Remember me?", variable = checkvalue)
checkbtn.grid(row = 6, column = 3)

#Submission Button
Button(text = "Submit", command = getvals).grid(row = 7, column = 3)

root.mainloop()
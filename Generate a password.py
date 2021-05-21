import random
Passwordlength = int(input("enter the length of password: "))
Samples="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_/-\+.-,*?"
Password_Suggestion = "".join(random.sample(Samples,Passwordlength ))
print(Password_Suggestion)
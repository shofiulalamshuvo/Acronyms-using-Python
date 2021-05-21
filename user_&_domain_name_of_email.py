youremail = input("Enter Your Email: ").strip()
Username = youremail[:youremail.index("@")]
Domain_Name = youremail[youremail.index("@")+1:]
format_ = (f"Your User Name is '{Username}' and Your Domain is '{Domain_Name}'")
print(format_)
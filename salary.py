sal=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
if(50000>=sal>=20000 or age<=25):
    print("You are eligible to take loan")
elif(sal>50000):
    print("Maximun loan amount is 50000")
else:
    print("You are not eligible")

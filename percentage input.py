m1=int(input("Enter Maths Mark:"))
m2=int(input("Enter physics Mark:"))
m3=int(input("Enter english Mark:"))
m4=int(input("Enter chemistry Mark:"))
total=m1+m2+m3+m4
avg=total/4
if(avg>70):
    name=input(("Enter your name:"))
    dept=input(("Enter your department name:"))
    loc=input(("Enter your location:"))
    print("You are eligible")
else:
    print("You are not eligible")

a=[]
sum=0
print("Enter 10 numbers:")
for i in range(10):
    num=int(input("Enter Number "+str(i+1)))
    a.append(num)
    sum=sum+num
    avg=sum/10
print("List:",a)
print("Sum:",sum)
print("Avg:",avg)

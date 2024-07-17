def calculate_averages():
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0
    while True:
        number = float(input("Enter the number: "))
        if number == -1:
            break
        elif number > 0:
            positive_sum += number
            positive_count += 1
        elif number < 0:
            negative_sum += number
            negative_count += 1
    if positive_count > 0:
        positive_avg = positive_sum / positive_count
    else:
        positive_avg = 0
    if negative_count > 0:
        negative_avg = negative_sum / negative_count
    else:
        negative_avg = 0
    print(f"The average of negative numbers is: {negative_avg:.2f}")
    print(f"The average of positive numbers is: {positive_avg:.2f}")
print("Enter -1 to exit...")
calculate_averages()

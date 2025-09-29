temperature = input("Enter temperature value (Degree): ")

min_temp = 20
room_temp = 27

if int(temperature) <= min_temp:
    print("The temperature value is less than the minimum temperature.")
    print("Drink Warm Water!")
elif int(temperature) <= room_temp & int(temperature) >= min_temp:
    print("The temperature value is greater than the min temperature & less than room temperature.")
    print("Drink Normal Water!")
else:
    print("The temperature value is greater than the minimum & room temperature.")

print("End")

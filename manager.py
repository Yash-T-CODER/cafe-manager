import time
from functools import reduce
print("Welcome to the py cafee")
print("\n")
time.sleep(2)

menu = {
    "coffee": 50,
    "tea": 30,
    "cold coffee": 70,
    "chocolate shake": 90,
    "burger": 100,
    "veg sandwich": 60,
    "cheese sandwich": 80,
    "french fries": 70,
    "momos": 90,
    "pizza": 150,
    "pasta": 120,
    "ice cream": 60,
    "brownie": 80
}
a=1
for i in menu:
    print(f"The {a} item is {i} and it's price is {menu[i]}")
    a=a+1
    time.sleep(1)
bill=[]
while True:
    time.sleep(3)
    order=input("What do you want to order:")
    bill.append(int(menu[order.lower().strip()]))
    if order.lower().strip() in menu:
        print("Your order has been taken,sir")
        a=input("Do you want anything else: ")
        if a.lower().strip() == "yes":
            continue
            
        elif a.lower().strip()=="no":
            print("Thank you for ordering sir ")
            break
        else:
            raise ValueError("Input should be in 'no' or 'yes'" )
    else:
        print("Sorry sir , the item you have ordered is not in our menu")

money=int(reduce((lambda x,y: x+y),bill))
print(f"Your bill is {money}")

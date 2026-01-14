print(10*3)
x=3
x+=2
print(x)
y=10>12
print(y)
z=10==10
print(z)
a=15!=15   
print(a)
price=5
print(price>10 or price<30)

temperature=9
if temperature>30:
    print("It's a hot day")
elif temperature<10: # comment:It's a cold day
    print("It's a cold day")
else:
    print("It's a lovely day")

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("You are " + str(converted) + " Lbs")
else:
    converted = weight * 0.45
    print("You are " + str(converted) + " Kgs")


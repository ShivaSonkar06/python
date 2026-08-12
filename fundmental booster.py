print("welcom the interactive personal data collector")

print()


name=input("please enter your name :")
age=int(input("please enter your age :"))
height=float(input("please enter your height in meters :"))
number=int(input("please enter your favorite number :"))

print()

print("thank you! here is the information we collected :")
print()

print("name:",name,type(name),id(name))
print("age:",age,type(age),id(age))
print("height:",height,type(height),id(height))
print("number:",number,type(number),id(number))

print()
birthyear= 2026 - age
print("your birth year is approximately:",birthyear,("based on your age of",age))

print()

print("thanks for using the personal data collector,goodbye!")




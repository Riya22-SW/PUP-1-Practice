# 8-10-2022
# 1.

# try:
#     print("try block")
#     num1=int(input("Enter first number"))
#     num2=int(input("Enter another number"))
#     res=num1/num2
# except:
#     print("Except block")
#     print("Number is not divisible by zero")
# else:
#     print("Else block")
#     print("output ",res)
# finally:
#     print("Exceptional handling program")


# 2.

try:
    num=int(input("Enter your age:"))
    if num<18:
        raise ValueError(num)
except ValueError:
    print(num, "is out of allowed range")
else:
    print(num, "is within the allowed range")


# try:
#     x = int(input("Enter a number: "))
#     square = x * x
#     print(f"Square: {square}")
#     x /= 0
# except ValueError:
#     print("Not a correct number")
# except ZeroDivisionError:
#     print("Couldn't divide by zero.")

file = open("file.txt", "w+")


try:
    for i in range(3):
        x = int(input("Enter a number: "))
        file.write(f"{x}\n")
except ValueError:
    print("This is not a number.")
except Exception:
    print("Unknown exception")
else:
    print("No errors detected.")
finally:
    file.close()
    print("File closed.")




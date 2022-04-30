# # Old variant
# def arithmetic(num1, num2, operation):
#     if operation == "+":
#         return num1 + num2
    
#     if operation == "-":
#         return num1 - num2

#     if operation == "*":
#         return num1 * num2
    
#     if operation == "/":
#         return num1 / num2

#     return "Неизвестная операция"


# # New variant
# def arithmetic(num1, num2, operation):
#     match operation:
#         case "+":
#             return num1 + num2
#         case "-":
#             return num1 - num2
#         case "*":
#             return num1 * num2
#         case "/":
#             return num1 / num2
#         case _:
#             return "Неизвестная операция"


# print(arithmetic(5, 3, '$'))


# # One more example
# def distanceToStart(*args):
#     match args:
#         case (a, b):
#             return (a**2 + b**2) ** 0.5
#         case (a, ):
#             return a
#         case _:
#             return None
        
        
# print(distanceToStart(3, 4))
# print(distanceToStart(6))
# print(distanceToStart())

command = input("Enter command: ").strip()
# go north/west/east/south
# sleep => ["sleep"]
# eat *

match command.split():
    case ["sleep"]:
        print("Sleeping...")
    case ["eat", food]:
        print(f"Eating {food}...")
    case ["go", "north" | "south" | "west" | "east" as direction]:
        print(f"Going {direction}...")
    case ["pay", value] if value.isnumeric():
        print(f"Paying {value} manats.")
    case _:
        print("Not a correct command.")


# command_list = command.split()
# if len(command_list) == 0:
#     print("Not a correct command")
# elif command_list[0] == "sleep":
#     print("Sleeping...")
# elif command_list[0] == "eat":
#     if len(command_list) > 1:
#         print(f"Eating {command_list[1]}")
#     else:
#         print("Not a correct command")
# elif command_list[0] == "go":
#     if len(command_list) == 1 or command_list[1] not in ("north", "east", "west", "south"):
#         print("Not a correct variant")
#     else:
#         print(f"Going {command_list[1]}")
# elif command_list[0] = "pay":
#     if len(command_list) == 1 or command_list[1].isnumeric() == False:
#         print("Not a correct command.")
#     else:
#         print(f"Paying {command_list[1]} manats.")
# else:
#     print("Not a correct variant")
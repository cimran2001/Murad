# Basics

str1 = 'Hello, world!'

str2 = "Hello, world!"

str3 = """Hello, world!""" # '''Hello, world!'''


# Control characters

# string = "\\n"
string = "Hello, \n\"\tworld\\n!"
print(string)


# Placeholder => %

'''
%s - string
%d - integer
%f - float
%f + %fj - complex
'''

name = "Murad"
surname = "Ismailov"
message = "Hello, %s %s. I'm %d years old!" 

# message1 = message % name
# print(message1)

# message2 = message % (name, surname)
# print(message2)

message3 = message % (name, surname, 15)
print(message3)


# Placeholder => format

message = "Hello, {1} {0}. I'm {2} years old!"

message1 = message.format(name, surname, 15)
print(message1)


# Placeholder => f

message = f"Hello, {name} {surname}. I'm {15} years old!"
print(message)

x = 5
print(f"{x=}")

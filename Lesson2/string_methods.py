sentence = "hello, WOrld!"

sentence1 = sentence.capitalize()
print(f"{sentence1=}")


sentence2 = sentence.casefold()
print(f"{sentence2=}")

sentence3 = sentence.lower()
print(f"{sentence3=}")

count_o = sentence.count("o")
print(f"{count_o=}")

count_all_o = sentence.casefold().count("o")
print(f"{count_all_o=}")

email = "\n c.imran2001@gmail.com     \t"
clear_email = email.strip() # removes white characters (" ", "\n", "\t")
print(f"{email=}")
print(f"{clear_email=}")

index = email.find("@")
print(f"{index=}")

not_found_index = email.find("fdshufdif") # returns -1
print(f"{not_found_index=}")

index = email.index("@")
print(f"{index=}")

# not_found_index = email.index("fdshufdif") # throws ValueError
# print(f"{not_found_index=}")

# print(email.index("@", 10, 19))

yandex_email = clear_email.replace("gmail", "yandex")
print(f"{yandex_email=}")

mail_ru_email = clear_email.replace("gmail.com", "mail.ru")
print(f"{mail_ru_email=}")

text = "abcAbcabc"
print(text.replace("abc", "def"))

number = "123a"
if number.isnumeric():
    print(int(number))
    
result = (clear_email.casefold() == "C.imran2001@gmail.com".casefold())
print(result)

if "@" not in clear_email:
    print("Not found.")

if clear_email.endswith(".com"):
    print("This site ends with .com!")
    
if clear_email.startswith("c.imran2001"):
    print("This is Imran's email!")


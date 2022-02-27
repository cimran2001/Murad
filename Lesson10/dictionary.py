# translator = {
#     "hello": "privet",
#     "bye": "poka", 
#     "thanks": "spasibo",
#     "idiot": "idiot"
# }

# word_in_english = input("Enter the word you want to translate: ")
# if word_in_english in translator.keys():
#     print(translator[word_in_english])
# else:
#     print("This word cannot be translated")


# empty_dict = dict()
# empty_dict = {} # dictionary


# x = {1, 2, 3}                        # set
# y = {4: "four", 5: "five", 6: "six"} # dictionary


capitals = {
    "USA": "Washington, D.C.", 
    "France" : "Paris", 
    "Japan" : "Tokyo", 
    "India" : "Delhi"
}
capitals["Azerbaijan"] = "Baku"
capitals["India"] = "New Delhi"

print(capitals.items())
# for key in capitals:
#     print("Key = " + key + ", Value = " + capitals[key])

# x = capitals.get("Azerbaijan", "Capital not found")
# print(x)
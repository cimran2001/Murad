database = {
	"c.imran2001": 25,
	"murad2006": 81
}

def hash(password: int) -> int:
	return password * password


login = input("Enter your login: ")
password = int(input("Enter your password: "))


if login not in database.keys():
	print("NOT A CORRECT USERNAME! ")
elif database[login] != hash(password):
	print("NOT A CORRECT PASSWORD! ")
else:
	print("YOU'VE ENTERED! ")

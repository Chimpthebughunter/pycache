cookies = int(input("How many cookies do you want?"))
choco = int(input("How many chocolate bars do you want?"))

snacks = cookies + choco

print("The number of snacks you are going to have are:")
print(snacks)

if snacks > 10:
    print("You are going to become diabetic if you eat that many snacks.")
else:
     print("That is a nice number of snacks!")

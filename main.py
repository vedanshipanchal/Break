word = input("Enter word:")

for i in word:
    if i=="A" or i=="a":
        print("found A")
        break
    else:
        print("not found")

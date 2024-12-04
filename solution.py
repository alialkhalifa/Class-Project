userInput = input("Enter a password: ")
dynamic_input = userInput
temp = ""
passwords = []
char_count = 0

with open("words.txt", "r") as f:
    for line in f.readlines():
        for char in dynamic_input:
             temp += char
             char_count += 1
             if temp == line:
                 passwords.append(temp)
                 dynamic_input = userInput[char_count:]
            
#While loop that runs until a full match is found
while True:
    #.strip() removes any whitespace before and after
    userInput = input("Enter a password: ").strip()
    dynamic_input = userInput
    passwords = []
    char_count = 0


    while dynamic_input:
        temp = ""
        #Used to ensure the correct word is stored if words are similar (hell and hello)
        longest_match = ""
        match_found = False

        with open("words.txt", "r") as f:
            for line in f:
                word = line.strip()
                if dynamic_input.startswith(word):
                    if len(word) > len(longest_match):
                        longest_match = word
                    match_found = True
        #If match is found add the word to the passwords lisst
        #update the counter variable and slice the dynamic_input so
        #so the found word is cut out
        if match_found:
            passwords.append(longest_match)
            char_count += len(longest_match)
            dynamic_input = userInput[char_count:]
        else:
            break
    #If the input is empty then the whole password has been found
    if not dynamic_input:
        #Testing
        print("Final passwords list:", passwords)
        break
    #If there is anything left then the user entered an invalid password.
    else:
        print("Invalid password. Enter new password")



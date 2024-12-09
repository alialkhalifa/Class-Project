#Liam Erickson
#Ali Al Khalifa
#““As a Hokie, I will conduct myself with honor and integrity at all times. I will not lie, cheat, or steal, not will I accept the actions of those who do.” -LE, -AK
import hashlib
import binascii
import time
import matplotlib.pyplot as plt # type: ignore

# Hash function with swertyPBKDF2-HMAC
def hash_password(password, algorithm):
    hashed_pwd = hashlib.pbkdf2_hmac(
        algorithm,  # Hash function
        password.encode('utf-8'),  # Password converted to binary
        'saltPhrase'.encode('utf-8'),  # Static salt
        100000  # Number of iterations
    )
    return binascii.hexlify(hashed_pwd)

# Load the dictionary into a list once
dict_array = []
sha256_time_array = []
sha512_time_array = []
guess_array = []
with open("words.txt", "r") as dict_file:
    for line in dict_file:
        dict_array.append(line.rstrip('\n'))

# Main loop to repeatedly take password input
dict_array.sort(key=lambda x: len(x), reverse=True)
while True:
    user_input = input("Enter a password (or 'q' to quit): ").strip()

    # Quit the program if 'q' is entered
    if user_input.lower() == 'q':
        print("Exiting program.")
        plt.plot(sha256_time_array, guess_array, 'ro', label='SHA256 (Red)')
        plt.plot(sha512_time_array, guess_array, 'bo', label='SHA512 (Blue)')
        plt.xlabel('Time to Crack (seconds)')
        plt.ylabel('Number of Guesses')
        plt.title('Password Cracking Time vs. Number of Guesses')
        dictionary_size = len(dict_array)
        legend_text = f"Dictionary Size: {dictionary_size} words"
        plt.legend(title=legend_text, loc='upper left')
        plt.show()
        break

    password = []
    r_input = user_input
    guess_count = 0
    start_time = time.time()
    # Break password into dictionary words
    while r_input:
        match_found = False
        for word in dict_array:
            guess_count+=1;
            if r_input.startswith(word):
                password.append(word)
                r_input = r_input[len(word):]
                match_found = True
                break
        if not match_found:
            print("Invalid password")
            break

    if not r_input:

        # Join password segments for full password hash
        full_password = ''.join(password)
        cracking_time = time.time() - start_time
        # Start timing for SHA256 hashing the full password
        start_sha256 = time.time()
        sha256_hash = hash_password(full_password, 'sha256').decode('utf-8')
        elapsed_sha256 = time.time() - start_sha256 + cracking_time
        sha256_time_array.append(elapsed_sha256)

        # Start timing for SHA512 hashing the full password
        start_sha512 = time.time()
        sha512_hash = hash_password(full_password, 'sha512').decode('utf-8')
        elapsed_sha512 = time.time() - start_sha512 + cracking_time
        sha512_time_array.append(elapsed_sha512)

        guess_array.append(guess_count)

        # Print results
        print(f"\nSHA256 Hash: {sha256_hash}")
        print(f"SHA512 Hash: {sha512_hash}\n")

        print(f"Cracked SHA256: {full_password}")
        print(f"Time to hash SHA256: {elapsed_sha256} seconds")

        print(f"Cracked SHA512: {full_password}")
        print(f"Time to hash SHA512: {elapsed_sha512} seconds\n")

print(sha256_time_array)
print(sha512_time_array)
print(guess_array)
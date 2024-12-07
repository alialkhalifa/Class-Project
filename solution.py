import hashlib
import binascii
import time

# Hash function with PBKDF2-HMAC
def hash_password(password, algorithm):
    hashed_pwd = hashlib.pbkdf2_hmac(
        algorithm,  # Hash function
        password.encode('utf-8'),  # Password converted to binary
        'saltPhrase'.encode('utf-8'),  # Static salt
        100000  # Number of iterations
    )
    return binascii.hexlify(hashed_pwd)

# Start timer
start = time.time()

# Input password
user_input = input("Enter a password: ").strip()

# Read words from dictionary and keeps it in a list
dict_array = []
with open("words.txt", "r") as dict_file:
    for line in dict_file:
        dict_array.append(line.rstrip('\n'))


password = []
r_input = user_input

while r_input:
    match_found = False
    for word in dict_array:
        if r_input.startswith(word):
            password.append(word)
            r_input = r_input[len(word):]
            match_found = True
            break
    if not match_found:
        print("Invalid password")
        break

if not r_input:
    print("Password broken into words:", password)
    for segment in password:
        # Hash with SHA256
        start_sha256 = time.time()
        sha256_hash = hash_password(segment, 'sha256').decode('utf-8')
        elapsed_sha256 = time.time() - start_sha256

        # Hash with SHA512
        start_sha512 = time.time()
        sha512_hash = hash_password(segment, 'sha512').decode('utf-8')
        elapsed_sha512 = time.time() - start_sha512

        # Print results
        print(f"\nCracked SHA256: {segment}")
        print(f"SHA256 Hash: {sha256_hash}")
        print(f"Time to crack: {elapsed_sha256} seconds")
        
        print(f"\nCracked SHA512: {segment}")
        print(f"SHA512 Hash: {sha512_hash}")
        print(f"Time to crack: {elapsed_sha512} seconds")


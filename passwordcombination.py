import itertools
import string
import time

def brute_force_attack(target_password,max_length):
    start_time = time.time()
    charset = string.ascii_letters + string.digits + string.punctuation
    for length in range(1,max_length + 1):
        for attempt in itertools.product(charset,repeat =length):
            attempt_password = ''.join(attempt)
            print(f"Trying password:{attempt_password}")

            if attempt_password == target_password:
                end_time = time.time()
                print("\nPassword found!")
                print(f"Password: {attempt_password}")
                print(f"Time taken: {end_time - start_time : 2f} seconds")
                return attempt_password
    print("\nPassword not found within the maximum length.")
    return None

target_password = input("Enter the password:")
max_length = 8
brute_force_attack(target_password,max_length)
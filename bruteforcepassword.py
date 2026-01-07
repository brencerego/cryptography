import itertools
import string

def brute_force_password(password, max_length=4):
    characters = string.ascii_letters + string.digits
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = "".join(guess)

            if guess == password:
                return f"Password '{password}' cracked in {attempts} attempts!"

    return "Password not found."

password = "abcd"
print(brute_force_password(password))

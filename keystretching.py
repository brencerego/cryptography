import os
import hashlib
import binascii

def stretch_key(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  

    iterations = 100_000
    key_length = 32

    derived_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        iterations,
        dklen=key_length
    )

    return salt, binascii.hexlify(derived_key).decode()

def verify_password(password, salt, stored_key):
    _, new_key = stretch_key(password, salt)
    return new_key == stored_key

if __name__ == "__main__":
    password = input("Enter password: ")
    salt, stretched = stretch_key(password)

    print("\nSalt:", binascii.hexlify(salt).decode())
    print("Stretched Key:", stretched)

    print("\nLogin Verification")
    check = input("Re-enter password: ")

    if verify_password(check, salt, stretched):
        print("Password Verified")
    else:
        print("Wrong Password")

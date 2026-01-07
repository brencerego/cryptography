import hashlib

target_password = input("Enter the target password:")
target_hash = hashlib.md5(target_password.encode()).hexdigest()

password_list = [
    '123456',
    'password',
    'password123',
    'admin'
]

def crack_hash(target_hash,dictionary):
    for password in dictionary:
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if hashed_password == target_hash:
            print(f"Password found: {password}")
            return password 
        
        print("Password not found!")
        return None
crack_hash(target_hash,password_list)
def brute_force_attack(password_list,target_password):
    for password in password_list:
        print(f"Trying password: {password}")

        if password == target_password:
            print(f"Password found:{password}")
            return True
    
    print("Password not found!")
    return False

if __name__ == "__main__":
    password_list = [
        "123456","password","123456789","12345678","qwerty","abc123","monkey","letmein","dragon","1111","basketball"
    ]

    target_password = input("Enter the target password:")
    print("starting brute force attack...")
    success = brute_force_attack(password_list,target_password)

    if success:
        print("Brute force attack successful!")
    else:
        print("Brute force attack failed.")
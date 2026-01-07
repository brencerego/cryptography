def is_password_common(password: str, common_passwords: list) -> bool:
    return password in common_passwords

common_passwords = ['123456','password','123456789','qwerty','abc123']
password = 'password'
if is_password_common(password, common_passwords):
    print("Password is too common!")
else:
    print("Password is not in the common list")
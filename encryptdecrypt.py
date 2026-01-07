def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


message = "Hello, World!"
shift_value = 3

encrypted_message = encrypt(message, shift_value)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted Message: {decrypted_message}")

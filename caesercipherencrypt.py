def caeser_cipher_encrypt(plaintext,shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha(): 
            if char.isupper():
                encrypted_char = chr((ord(char)-ord('A') + shift)%26 + ord('A'))
            else:
                encrypted_char = chr((ord(char)-ord('a') + shift)%26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text +=char
    return encrypted_text

plaintext=input("enter the text: ")
shift=int(input("enter the shift value: "))

encrypted_text=caeser_cipher_encrypt(plaintext,shift)
print("encrypted text",encrypted_text)
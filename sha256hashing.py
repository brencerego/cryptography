import hashlib
def hash_string(text):
    hasher=hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()

text=input("enter the text to hash: ")

hash_value=hash_string(text)
print("original text: ",text)
print("SHA-256 hash: ",hash_value)
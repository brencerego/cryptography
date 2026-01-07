import hashlib

def get_sha256_hash(text):
    sha_signature = hashlib.sha256(text.encode()).hexdigest()
    return sha_signature

text = "Cybersecurity is important!"
print(f"Text:{text}")
print(f"SHA-256 Hash: {get_sha256_hash(text)}")

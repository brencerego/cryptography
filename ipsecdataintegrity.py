import hashlib
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

data=input("enter data to be send: ")
hash_value=generate_hash(data)
print("generated hash",hash_value)
received_data=input("enter received data: ")
received_hash=generate_hash(received_data)

if received_hash==hash_value:
    print("integrity verified: data not modified")
else:
    print("integrity failed: data modified")
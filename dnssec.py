import hashlib

def sign_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

orginal_domain = input("enter orginal domain name: ")
signature=sign_data(orginal_domain)
print("\nGenerated DNS signature: ", signature)

received_domain=input("\nenter received domain name: ")
verify_signature=sign_data(received_domain)

if verify_signature==signature:
    print("\nDNSSEC verifivation successful: data is authentic")
else:
    print("\nDNSSEC verifivation failed: data has been modified")
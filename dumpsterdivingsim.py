def dumpster_diving(file_content):
    sensitive_info = ['password','credit card','ssn','account number']
    found_info = [info for info in sensitive_info if info in file_content.lower()]
    if found_info:
        return f"Sensitive information found: {found_info}"
    else:
        return "No sensitive information detected"
    
file_data = "My password is 123456 and my account number is 987654321"
print(dumpster_diving(file_data))
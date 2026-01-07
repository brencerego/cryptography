def detect_identity_fraud(email):
    legit_domains = ['gmail.com','yahoo.com','outlook.com']
    domains = email.split('@')[-1]
    if domains not in legit_domains:
        return "Potential identity fraud detected! Suspicious email domain"
    else:
        return "Email seems legitimate"
    
email = "user@fraudulent-domain.com"
print(detect_identity_fraud(email))

    
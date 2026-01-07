def detect_phishing(email, content):
    phishing_keywords = ['win', 'free', 'urgent', 'click', 'claim', 'password']

    found_keywords = [
        word for word in phishing_keywords
        if word in content.lower()
    ]

    if found_keywords:
        return f"Potential phishing detected! Keywords found: {found_keywords}"
    else:
        return "Email seems safe"

email_content = "Click here to win a free iPhone by updating your password!"
print(detect_phishing("sender@example.com", email_content))

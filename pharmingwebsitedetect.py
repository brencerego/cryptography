def detect_pharming(url):
    known_legit_domains = ['https://www.bank.com','https://www.shop.com']
    if url not in known_legit_domains:
        return "Potential pharming attack detected! Suspicipous URL"
    else:
        return "URL seems safe"
    
url = "https://www.fake-bank.com"
print(detect_pharming(url))
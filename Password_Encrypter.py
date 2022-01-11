from cryptography.fernet import Fernet


def encode(plain_text):
    key = Fernet.generate_key()
    fer = Fernet(key)
    encrypted = fer.encrypt(plain_text)
    return encrypted


unsecured_key = bytes(input("Enter your password to encrypt it: "), "UTF-8")
secured_key = encode(unsecured_key)

print(f"Your encrypted password: {secured_key}")

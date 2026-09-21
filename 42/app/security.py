from pwdlib import PasswordHash

hasher = PasswordHash.recommended()

def hash_password(password: str):
    return hasher.hash(password)

def verify_password(password: str, hashed_password: str):
    return hasher.verify(password, hashed_password)
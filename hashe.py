# password_utils.py
import random
import string
import hashlib

def generate_password():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

def hash_password(password):
    h = hashlib.new("sha256")
    h.update(password.encode("utf-8"))
    return h.hexdigest()
import hashlib

common_passwords = []
user_hash_dict = {}

with open('data/common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()

with open('data/username_hashes.txt', 'r') as f:
    for line in f.read().splitlines():
        username, stored_hash = line.split(":")
        user_hash_dict[username] = stored_hash

for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    for username, stored_hash in user_hash_dict.items():
        if hashed_password == stored_hash:
            print(f"HASH FOUND\n{username}:{password}")

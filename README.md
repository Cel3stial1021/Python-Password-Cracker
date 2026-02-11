# Python-Password-Cracker
Python SHA-256 hash matching lab that cracks weak passwords using a wordlist and a username:hash file (education/demo).
# Hash Matching Password Cracker (SHA-256) — Mini Lab

This project is a small Python lab that demonstrates how password hashing works and how weak passwords can be identified when you have:
1) a list of common passwords, and  
2) a list of usernames with hashed passwords.

The script hashes each candidate password using SHA-256 and checks whether the hash matches any stored user hash. If a match is found, it prints the username and the cracked password.

> Educational use only: this is meant for learning and security awareness.

---

## Files in this repository

### `src/password_cracker.py`
Reads:
- `data/common_passwords.txt`
- `data/username_hashes.txt`

Then:
- hashes every password candidate with SHA-256
- compares it against each user’s stored hash
- prints matches in the format: `username:password`

### `src/generate_hashes.py`
A simple helper script that shows how to SHA-256 hash a string in Python.

### `data/username_hashes.txt`
A text file with lines formatted like:

`username:hash`

Example:
`jsmith:0b14d...`

### `data/common_passwords.txt`
A wordlist of password candidates (one per line).

---

## Requirements
- Python 3.8+ (any recent Python 3 should work)
- No extra libraries needed (uses Python’s built-in `hashlib`)

---

## How to run

From the project root:

### Option A: Run the cracker
```bash
python3 src/password_cracker.py

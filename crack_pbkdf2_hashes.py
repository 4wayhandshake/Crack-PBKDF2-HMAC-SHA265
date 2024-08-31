#!/usr/bin/env python3

import hashlib
import os
import sys
from concurrent.futures import ThreadPoolExecutor

usage_str = '''

Attempts to crack a file with password hashes, using PBKDF2-HMAC-SHA256 hashing.
Defaults to 50,000 iterations and a key length of 50

Don\'t use too large of a wordlist. This program is NOT memory optimized!

Hashes file should have lines the format username:hash:salt
For example...
admin:1bf0b7ef1cf076c5fc0d76e140788a91b52828b1c384791839fd6e9996d3bbf5c91b8eee6bd5081e42085ed0be779c2ef86d:a45c43d36dce3076158b19c2c696ef7b

'''
    
def usage():
    print(f'Usage: {sys.argv[0]} <wordlist> <hashes_file> [num_iterations] [key_length]{usage_str}')
    sys.exit()
    
if len(sys.argv) < 3 or '-h' in sys.argv:
    usage()

wordlist_path = sys.argv[1]
hashes_path = sys.argv[2]
num_iterations = 50000 if len(sys.argv) < 4 else int(sys.argv[3])
key_length = 50 if len(sys.argv) < 5 else int(sys.argv[4])

def load_hashes(path):
    hashes = []
    with open(path, 'r') as f:
        for line in f:
            usr, passwd, salt = line.strip().split(':')
            hashes.append({
                'username': usr,
                'hash': bytes.fromhex(passwd),
                'salt': bytes.fromhex(salt)
            })
    return hashes

def pbkdf2_hash(word, salt):
    # hash a single word using PBKDF2 and the provided salt
    return hashlib.pbkdf2_hmac('sha256', word.encode(), salt, num_iterations, dklen=key_length)
    
def check_guess(guess):
    for hash_obj in hashes:
        s = hash_obj['salt']
        h = hash_obj['hash']
        hashed_guess = pbkdf2_hash(guess, s)
        #print(f"Checking match: {guess}\nSalt: {s.hex()}\nHash: {hashed_guess.hex()}\nPass: {h.hex()}\n")
        if hashed_guess == h:
            u = hash_obj['username']
            print(f'FOUND A MATCH -- {u} : {guess}')

hashes = load_hashes(hashes_path)
lines = []
with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
    lines = list(map(lambda l: l.strip(), file.readlines()))
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(check_guess, lines)

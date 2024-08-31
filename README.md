# Crack-PBKDF2-HMAC-SHA265
Attempts to crack a file with password hashes, using PBKDF2-HMAC-SHA256 hashing.

Defaults to **50,000 iterations** and a key **length of 50**

> Don't use too large of a wordlist. This program is **NOT memory optimized!**
>
> I wouldn't go past 20,000ish lines

Hashes file should have lines the format `username:password_hash:salt`

`
admin:1bf0b7ef1cf076c5fc0d76e140788a91b52828b1c384791839fd6e9996d3bbf5c91b8eee6bd5081e42085ed0be779c2ef86d:a45c43d36dce3076158b19c2c696ef7b`

### Usage:

```bash
crack_pbkdf2_hashes.py <wordlist> <hashes_file> [num_iterations] [key_length]
```


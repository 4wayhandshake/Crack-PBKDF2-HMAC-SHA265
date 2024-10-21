# Crack-PBKDF2-HMAC-SHA265
Tools for processing password hashes made using Werkzeug, using PBKDF2-HMAC-SHA256 hashing.

This repo contains two scripts:
 * `crack_pbkdf2-sha256_hashes.py`
   Attempts to crack hashes directly
 * `transform_pbkdf2-sha256_hashes.py`
   Transforms hashes into a format usable by **hashcat**.

## Usage:

### crack_pbkdf2-sha256_hashes.py

```bash
crack_pbkdf2-sha256_hashes.py <wordlist> <hashes_file> [num_iterations] [key_length]
```

Hashes file should have lines in the format `username:password_hash:salt`, like this:

`admin:1bf0b7ef1cf076c5fc0d76e140788a91b52828b1c384791839fd6e9996d3bbf5c91b8eee6bd5081e42085ed0be779c2ef86d:a45c43d36dce3076158b19c2c696ef7b`

Defaults to **50,000 iterations** and a key **length of 50**

> Don't use too large of a wordlist. This program is **NOT memory optimized!**. I wouldn't go past 20,000ish lines

### transform_pbkdf2-sha256_hashes.py

```bash
transform_pbkdf2-sha256_hashes.py <input_hashes_filepath> <output_hashes_filepath>
```

Input hashes file should have lines in the format `pbkdf2:sha256:iterations$salt_base64$hash_hex`, like this:

`pbkdf2:sha256:600000$NJmGroHCwx0TCl0z$c10a63e2d93316572ba9d01d674fd720f1df549eb5cf5a35491aec6773d55387`

Will ignore lines that start with a `#` comment.




Please :star: this repo if you found it useful!


---

Enjoy,

:handshake::handshake::handshake::handshake:
@4wayhandshake

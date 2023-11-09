# sprig-aes

Library and CLI to encrypt and decrypt text using AES CBC mode.

Note that the implementation is ported from:

1. http://masterminds.github.io/sprig/crypto.html#encryptaes
2. http://masterminds.github.io/sprig/crypto.html#decryptaes

## Using The Library

```py3
from sprig_aes import sprig_encrypt_aes

key = "6Jsv61H7fbkeIkRvUpnZ98fu"
enc_text = sprig_encrypt_aes("a secret message", key)
dec_text = sprig_decrypt_aes(enc_text, key)
```

## Using The CLI

```sh
sprig-aes encrypt 'a secret message' --key 6Jsv61H7fbkeIkRvUpnZ98fu
sprig-aes decrypt 'zLBGM41dAfA2JuIkVHRKaxydwr8+IClmaf69wqQgAd8=' --key 6Jsv61H7fbkeIkRvUpnZ98fu
```

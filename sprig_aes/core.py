import base64
import os
from typing import AnyStr

from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes


def _as_bytes(value: AnyStr) -> bytes:
    if isinstance(value, str):
        return value.encode()
    return value


def _fill_bytes(value: AnyStr) -> bytes:
    # fill the bytes and collect the first 32 bytes at maximum
    return (_as_bytes(value) + bytes(32))[:32]


class SprigAES:
    """This class encrypt/decrypt text that is compatible with Sprig AES."""

    BLOCK_SIZE = 16

    @classmethod
    def encrypt(cls, text: AnyStr, key: AnyStr) -> bytes:
        key_bytes = _fill_bytes(key)
        text_bytes = _as_bytes(text)

        # fill the block size of text_bytes
        padding = cls.BLOCK_SIZE - len(text_bytes) % cls.BLOCK_SIZE
        text_bytes += bytes(chr(padding) * padding, "utf-8")

        iv = os.urandom(cls.BLOCK_SIZE)
        # Sprig Go prepend the ciphertext with iv
        ciphertext = iv + text_bytes
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))

        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(ciphertext) + encryptor.finalize()
        return base64.b64encode(encrypted_text)

    @classmethod
    def decrypt(cls, text: AnyStr, key: AnyStr) -> bytes:
        key_bytes = _fill_bytes(key)
        ciphertext = base64.b64decode(_as_bytes(text))

        iv = ciphertext[:cls.BLOCK_SIZE]
        text_bytes = ciphertext[cls.BLOCK_SIZE:]

        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))

        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(text_bytes) + decryptor.finalize()

        # unpad decrypted_text to get the actual text
        decrypted_text_len = len(decrypted_text)
        unpadding = int(decrypted_text[decrypted_text_len - 1])
        return decrypted_text[:(decrypted_text_len - unpadding)]


# shortcut to encryption method
sprig_encrypt_aes = SprigAES.encrypt

# shortcut to decryption method
sprig_decrypt_aes = SprigAES.decrypt

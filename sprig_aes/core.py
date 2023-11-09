import base64
import os
import typing as _t

from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes


class SprigAES:
    """This class encrypt/decrypt text that is compatible with Sprig AES."""

    BLOCK_SIZE = 16

    @staticmethod
    def _as_bytes(value: _t.AnyStr) -> bytes:
        if isinstance(value, str):
            return value.encode()
        return value

    @classmethod
    def _fill_bytes(cls, value: _t.AnyStr) -> bytes:
        # fill the bytes and collect the first 32 bytes at maximum
        return (cls._as_bytes(value) + bytes(32))[:32]

    @classmethod
    def encrypt(cls, text: _t.AnyStr, key: _t.AnyStr) -> bytes:
        key_bytes = cls._fill_bytes(key)
        text_bytes = cls._as_bytes(text)

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
    def decrypt(cls, text: _t.AnyStr, key: _t.AnyStr) -> bytes:
        key_bytes = cls._fill_bytes(key)
        ciphertext = base64.b64decode(cls._as_bytes(text))

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

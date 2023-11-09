import pytest


@pytest.mark.parametrize("text, key, encrypted_text", [
    ("a secret message", "6Jsv61H7fbkeIkRvUpnZ98fu", b"zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C"),
    (b"random text", b"6Jsv61H7fbkeIkRvUpnZ98fu", b"zLBGM41dAfA2JuIkVHRKaxydwr8+IClmaf69wqQgAd8="),

])
def test_aes_encrypt(text, key, encrypted_text):
    from sprig_aes.core import sprig_encrypt_aes
    assert sprig_encrypt_aes(text, key) == encrypted_text


@pytest.mark.parametrize("encrypted_text, key, text", [
    ("zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C", "6Jsv61H7fbkeIkRvUpnZ98fu", b"a secret message"),
    (b"zLBGM41dAfA2JuIkVHRKaxydwr8+IClmaf69wqQgAd8=", b"6Jsv61H7fbkeIkRvUpnZ98fu", b"random text"),
])
def test_aes_decrypt(encrypted_text, key, text):
    from sprig_aes.core import sprig_decrypt_aes
    assert sprig_decrypt_aes(encrypted_text, key) == text

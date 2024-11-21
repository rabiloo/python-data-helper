"""Security file."""

import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key(key: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100_000, backend=default_backend())
    return kdf.derive(key.encode())


def file_encrypt(input_file_path: str, output_file_path: str, secret_key: str):
    """Encrypt content with aes."""
    with open(input_file_path, "rb") as file:
        content = file.read()

    salt = os.urandom(16)
    iv = os.urandom(16)

    aes_key = derive_key(secret_key, salt=salt)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())

    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padder_plaintext = padder.update(content) + padder.finalize()

    ciphertext = encryptor.update(padder_plaintext) + encryptor.finalize()
    encrypted_data = salt + iv + ciphertext

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, "wb") as file:
        file.write(encrypted_data)


def file_decrypt(input_file_path: str, output_file_path: str, secret_key: str):
    """Decrypt content with aes."""
    with open(input_file_path, "rb") as file:
        content = file.read()

    salt = content[:16]
    iv = content[16:32]
    ciphertext = content[32:]

    aes_key = derive_key(secret_key, salt=salt)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, "wb") as file:
        file.write(decrypted_data)


def folder_encrypt(input_folder_path: str, output_folder_path: str, secret_key: str):
    """Encrypt folder content with aes."""
    for root, _, files in os.walk(input_folder_path):
        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(root.replace(input_folder_path, output_folder_path), file)
            file_encrypt(input_file_path, output_file_path, secret_key)


def folder_decrypt(input_folder_path: str, output_folder_path: str, secret_key: str):
    """Decrypt folder content with aes."""
    for root, _, files in os.walk(input_folder_path):
        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(root.replace(input_folder_path, output_folder_path), file)
            file_decrypt(input_file_path, output_file_path, secret_key)

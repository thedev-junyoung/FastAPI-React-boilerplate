from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

# 설정 상수
SALT_SIZE = 16
HASH_ALGORITHM = hashes.SHA256()
ITERATIONS = 100_000
KEY_LENGTH = 32

def get_password_hash(password: str) -> str:
    """
    주어진 비밀번호를 해시하여 반환합니다.

    Args:
    password (str): 해싱할 원본 비밀번호

    Returns:
    str: 해싱된 비밀번호
    """
    salt = os.urandom(SALT_SIZE)
    kdf = PBKDF2HMAC(
        algorithm=HASH_ALGORITHM,
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return urlsafe_b64encode(salt + key).decode()

def verify_password(password: str, hashed_password: str) -> bool:
    """
    주어진 비밀번호가 해시된 비밀번호와 일치하는지 검증합니다.

    Args:
    password (str): 원본 비밀번호
    hashed_password (str): 해싱된 비밀번호

    Returns:
    bool: 비밀번호 일치 여부
    """
    decoded_hashed_password = urlsafe_b64decode(hashed_password.encode())
    salt = decoded_hashed_password[:SALT_SIZE]
    key = decoded_hashed_password[SALT_SIZE:]
    kdf = PBKDF2HMAC(
        algorithm=HASH_ALGORITHM,
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    try:
        kdf.verify(password.encode(), key)
        return True
    except:
        return False

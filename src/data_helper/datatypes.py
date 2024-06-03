def str2bytes(string: str, encoding: str = "utf-8") -> bytes:
    """Convert a string to bytes"""
    return string.encode(encoding)


def bytes2str(byte: bytes) -> str:
    """Convert a byte stream into a string"""
    return byte.decode("utf-8")

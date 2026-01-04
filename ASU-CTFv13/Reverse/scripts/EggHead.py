import codecs

# Target bytes from the decompiled file
KEY_TARGET = bytes.fromhex('c1 a0 c0 c3 9d b5 cf ca cf c2 a0 c8 9f cf c4 a0 b5 cf cc a0 b5')
IV_TARGET = bytes.fromhex('9a cb 99 c9 9b 99 da 99')

def rot47(s: str) -> str:
    """Apply rot47 to a string."""
    out = []
    for c in s:
        o = ord(c)
        if 33 <= o <= 126:
            out.append(chr(33 + (o - 33 + 47) % 94))
        else:
            out.append(c)
    return ''.join(out)

def decode_key(target_bytes):
    # Reverse the XOR with 255
    xored = bytes(b ^ 255 for b in target_bytes)
    # Convert bytes to string for rot47
    xored_str = xored.decode('ascii')
    # Reverse rot47 (rot47 is its own inverse)
    return rot47(xored_str)

def decode_iv(target_bytes):
    # Reverse the XOR with 170
    xored = bytes(b ^ 170 for b in target_bytes)
    # Convert bytes to string for rot13
    xored_str = xored.decode('ascii')
    # Reverse rot13 (rot13 is its own inverse)
    return codecs.decode(xored_str, 'rot_13')

# Recover the credentials
key = decode_key(KEY_TARGET)
iv = decode_iv(IV_TARGET)

print(f"Key: {key}")
print(f"IV:  {iv}")
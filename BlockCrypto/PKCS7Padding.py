# -*- coding: utf-8 -*-
"""
Implement PKCS#7 padding

Mikkel Højlund Larsen
"""


def PKCS7Pad(block_size: int, plaintext: bytes):
    padding_size = block_size -(len(plaintext) % block_size)
    padding = (chr(padding_size)*padding_size).encode()
    return plaintext + padding

def PKCS7Strip(data: bytes):
    paddinglength = data[-1]
    return data[:-paddinglength]

"""
TEST
"""
#subject = b"YELLOW SUBMARINE"
#print(PKCS7Padding(20, subject))


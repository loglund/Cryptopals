# -*- coding: utf-8 -*-
"""
Implementation of repeating-key XOR.

Mikkel Højlund Larsen
"""

line = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
k = b"ICE"



def repeatingXOR(message: bytes, key):
    j = 0
    output_bytes = b''
    for byte in message:
        output_bytes += bytes([byte ^ key[j]])
        if (j + 1) == len(key):
            j = 0
        else:
            j += 1
    return output_bytes

repeatingXOR(line, k)


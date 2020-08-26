# -*- coding: utf-8 -*-
"""
Fixed XOR function

Takes two equal length buffers in hex-code and outputs their XOR combination. 

Mikkel Højlund Larsen
"""
import base64

def fixedXOR(string1: bytes, string2: bytes):
    return(bytes([x ^ y for (x,y) in zip(string1, string2)]))

"""
TEST
"""
#print(fixedXOR(bytes.fromhex("1c0111001f010100061a024b53535009181c"),bytes.fromhex("686974207468652062756c6c277320657965")))


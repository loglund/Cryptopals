# -*- coding: utf-8 -*-
"""
Hex to Base-64 conversion

Mikkel Højlund Larsen
"""
import base64

def hexTo64(hexstring:str):
    hex_data = bytes.fromhex(hexstring)
    b64string = base64.b64encode(hex_data)
    print(b64string)
    return b64string

hexTo64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

# -*- coding: utf-8 -*-
"""
Implementation of CBC mode (Cipher Block Chaining) with ECB encryption

Mikkel Højlund Larsen
"""
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Basics.AESinECB import AES_ECB_Encrypt, AES_ECB_Decrypt
import base64
from PKCS7Padding import PKCS7Pad, PKCS7Strip
from math import ceil
from Basics.FixedXOR import fixedXOR


def chunkSplitter(text: bytes, block_size: int):
    numberChunks = ceil(len(text) / block_size)
    return [text[block_size*i : block_size*(i+1)] for i in range(numberChunks)]

def AESECBinCBC_encrypt(IV: bytes, plaintext: bytes, key: bytes ):
    result = b''
    prevBlock = IV
    paddedPlaintext = PKCS7Pad(16, plaintext)
    blocks = chunkSplitter(paddedPlaintext, 16)
    for block in blocks:
        to_encrypt = fixedXOR(prevBlock, block)
        new_cblock = AES_ECB_Encrypt(to_encrypt, key)
        result += new_cblock
        prevBlock = new_cblock
    return result

def AESECBinCBC_decrypt(IV: bytes, ctext: bytes, key: bytes):
    result = b''
    prevBlock = IV
    paddedCiphertext = PKCS7Pad(16, ctext)
    blocks = chunkSplitter(paddedCiphertext, 16)
    for block in blocks:
            to_decrypt = AES_ECB_Decrypt(block, key)
            result += fixedXOR(to_decrypt, prevBlock)
            assert len(result)!= 0
            prevBlock = block
            print(result)
    return PKCS7Strip(result)

#TEST
    
#ciphertext = base64.b64decode(open("CBC.txt").read())
#inivec = bytes(chr(0), "utf-8")
#k = b"YELLOW SUBMARINE"

#print(AESECBinCBC_decrypt(inivec, ciphertext, k))
    
    
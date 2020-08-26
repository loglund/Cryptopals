# -*- coding: utf-8 -*-
"""
AES128 in ECB mode. Decryption knowing key "YELLOW SUBMARINE".

Mikkel Højlund Larsen
"""
from Crypto.Cipher import AES
import base64
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from BlockCrypto.PKCS7Padding import PKCS7Pad,PKCS7Strip

def ECB_EncryptBlock(key, block):
    assert(len(block) == 16)
    suite = AES.new(key, AES.MODE_ECB)
    return suite.encrypt(block)

def ECB_DecryptBlock(key, block):
    assert(len(block) == 16)
    suite = AES.new(key, AES.MODE_ECB)
    return suite.decrypt(block)

def getBlocks(bytes_, blocksize=16):
    return [bytes_[i:i+blocksize] for i in range(0, len(bytes_), blocksize)]

"""
Padded AES in ECB encryption and decryption
"""
def ECB_Encrypt(key, plaintext):
    blocks = getBlocks(PKCS7Pad(16,plaintext))
    ciphertext = bytearray()
    for block in blocks:
        ciphertext.extend(ECB_EncryptBlock(key, block))
    return bytes(ciphertext)

def ECB_Decrypt(key, ciphertext):
    blocks = getBlocks(ciphertext)
    plaintext = bytearray()
    for block in blocks:
        plaintext.extend(ECB_DecryptBlock(key, block))
    return PKCS7Strip(bytes(plaintext))

#TEST


#f = open("AEScipher.txt")
#ciphertext = base64.b64decode(f.read())


#k = b'YELLOW SUBMARINE'
#print(AES_ECB_Decrypt(ciphertext,k))


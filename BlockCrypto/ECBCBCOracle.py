# -*- coding: utf-8 -*-
"""
ECB/CBC detection Oracle

Mikkel Højlund Larsen
"""
import random
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Basics.AESinECB as aie
import CBCmode as cbc
import Basics.DetectECBinAES as eia

def Oracle_encrypt(plaintext: bytes, mode = None):
    key = os.urandom(16)
    frontrandom = os.urandom(random.randint(5,10))
    backrandom = os.urandom(random.randint(5,10))
    to_encrypt = frontrandom + plaintext + backrandom
    
    if mode == None:
        mode = random.choice(['ECB', 'CBC'])
    if mode == 'ECB':
        return aie.Pad_AES_ECB_Encrypt(to_encrypt, key)
    if mode == 'CBC':
        iv = os.urandom(16)
        return cbc.AESECBinCBC_encrypt(to_encrypt, iv, key)



# -*- coding: utf-8 -*-
"""
Byte-at-a-time ECB Decryption using the Oracle

Mikkel Højlund Larsen
"""
import random
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Basics.AESinECB as aie
import base64
import Basics.DetectECBinAES as dea
from sys import stdout
secret = base64.b64decode(
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
    "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
    "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
    "YnkK")
k = os.urandom(16)


def discoverBlockSize(oracle):
    size = len(oracle(bytes()))
    i = 1
    while size == len(oracle(bytes([0x42] * i))):
        i += 1
    
    next_size = len(oracle(bytes([0x42] * i)))
    return next_size - size

def ECB_Check(oracle, blocksize):
    ciphertext = oracle(bytes([0x42] * 3 * blocksize))
    blocks = aie.getBlocks(ciphertext, blocksize)
    uniqueBlocks = len(set(blocks))
    return uniqueBlocks != len(blocks)

def oracle(input_):
    return aie.ECB_Encrypt(k, input_+secret)

"""
We will use 0x42 as our padding byte (corresponds to "B" in ASCII)
"""

PADDING_BYTE = 0x42

def getLastKnownBlock(plaintext: bytes, blocksize: int):
    last_plaintext_block = plaintext[-blocksize:]
    
    padding = bytes([PADDING_BYTE]*(blocksize- len(last_plaintext_block)))
    
    guessing_block = padding + last_plaintext_block
    assert(len(guessing_block) == blocksize)
    
    return guessing_block

def targetNextByte(plaintext: bytes, blocksize: int):
    index = len(plaintext)
    blockindex = index // blocksize
    indexInBlock = index % blocksize
    
    padding = blocksize - 1 - indexInBlock
    pad = bytes([PADDING_BYTE]* padding)
    return(pad, blockindex)

"""
TEST 
"""

blocksize = discoverBlockSize(oracle)
assert(16 == blocksize)

assert(ECB_Check(oracle, blocksize))

bytesCount = len(oracle(bytes()))
plaintext = bytearray()

for _ in range(bytesCount):
    lastKnownBlock = getLastKnownBlock(plaintext, blocksize)
    
    input_, targetBlockIndex = targetNextByte(plaintext, blocksize)
    ciphertext = oracle(input_)
    
    targetBlock = aie.getBlocks(ciphertext)[targetBlockIndex]
    
    prefix = lastKnownBlock[1:]
    
    foundMatch = False
    for byte in range(256):
        ciphertextGuess = oracle(prefix + bytes([byte]))
        guess = aie.getBlocks(ciphertextGuess)[0]
        
        if targetBlock == guess:
            foundMatch = True
            plaintext.append(byte)
            stdout.write(chr(byte))
            stdout.flush()
            break
    if not foundMatch:
        assert(plaintext[-1] == 0x1)
        plaintext = plaintext[:-1]
        break

assert(plaintext == secret)
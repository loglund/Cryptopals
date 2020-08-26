# -*- coding: utf-8 -*-
"""
Single-byte XOR Cipher attack

Uses occurences of letters in the english language

Mikkel Højlund Larsen
"""
encoding = 'utf-8'

def SingleByteXOR(string1: bytes, key: int):
    return bytes([b ^ key for b in string1])
    

from collections import Counter
occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

dist_english = list(occurance_english.values())

def computeFittingQuotient(string1: bytes):
    counter = Counter(string1)
    dist_text = [
            (counter.get(ord(ch),0)*100) / len(string1)
            for ch in occurance_english
            ]
    return sum([abs(a-b) for a,b in zip(dist_english, dist_text)]) / 100
    


def SBXORDecipher(string1: bytes):
    originalText, encryptionKey, minFQ = None, None, None
    for k in range(256):
        Text = SingleByteXOR(string1, k)
        FQ = computeFittingQuotient(Text)
        if minFQ is None or FQ < minFQ:
            encryptionKey, originalText, minFQ = k, Text, FQ
    return originalText, encryptionKey, minFQ



SBXORDecipher(bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
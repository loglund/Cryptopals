# -*- coding: utf-8 -*-
"""
Breaking Repeating-key XOR.

Mikkel Højlund Larsen
"""
import math
import base64
import SingleByteXorCipher as sbxc
import RepeatingKeyXOR as rkx

f = open("Challenge6.txt")
ciphertext = base64.b64decode(f.read())

def HammingDistance(str1: bytes, str2: bytes):
    dist = 0
    for i in range(len(str1)):
        dist += bin(str1[i] ^ str2[i]).count('1')
    return dist

def RepeatingXORDecrypt(string: bytes, size_min, size_max):
    min_dist = 0
    for i in range(size_min, size_max):
        comp1 = string[0:i]
        comp2 = string[i:i*2]
        comp3 = string[2*i:3*i]
        comp4 = string[3*i:4*i]
        ham_norm = (HammingDistance(comp1, comp2)
        + HammingDistance(comp1,comp3)
        + HammingDistance(comp1,comp4)
        + HammingDistance(comp2,comp3)
        + HammingDistance(comp2,comp4)
        + HammingDistance(comp3,comp4) )/i
        print(ham_norm)
        if min_dist == 0 or ham_norm < min_dist:
            min_dist = ham_norm
            keysize = i
        print(keysize, min_dist)
    blocklist=[]
    for i in range(math.floor(len(string)/keysize)):
        testlist = []
        testlist.append(string[i*keysize : i*keysize+keysize])
        blocklist.append(testlist)
    transblocklist = []
    for j in range(keysize):
        list1 = []
        for i in range(len(blocklist)):
            for k in range(len(blocklist[i])):
                list1.append(chr(blocklist[i][k][j]))
            ''.join(list1).replace(',','')
        transblocklist.append(''.join(list1).replace(',',''))
    for i in range(len(transblocklist)):
        transblocklist[i] = bytes(transblocklist[i], "utf-8")
    keylist = []
    for j in range(len(transblocklist)):
        keylist.append(sbxc.SBXORDecipher(transblocklist[j])[1])
    result = rkx.repeatingXOR(string, keylist)
    print(result, keylist)
    return result, keylist
    
RepeatingXORDecrypt(ciphertext, 2, 40)



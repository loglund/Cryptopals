# Cryptopals
Challenges from Cryptopals.com in Python

## Set 1 - Basics

- [x] [1. Hex to base-64 conversion](Basics/HexTo64.py)
- [x] [2. Fixed Xor operation](Basics/FixedXOR.py)
Implentation of a equal-length XOR-function. Takes two equal length buffers as input and outputs their XOR result.
- [x] [3. Single Byte XOR Cipher](Basics/SingleByteXorCipher.py)
Code to decrypt and find the key of a Single-byte XOR cipher using statistics.

- First we infer the probabilities of the occurence of a specific letter in the english language in a dictionary (not divided by 100 yet)
This is used to compute a fitting quotient by counting the occurence of english letters in a given string (in ASCII)

- To break the single-byte XOR cipher, we then compute this fitting quotient of the encrypted message XOR'ed with all the possible characters in the ASCII table (the extended one 256 possible characters)

- The XOR'ed string with the minimum frequency is chosen to be the plaintext and the key is the character XOR'ed against the corresponding ciphertext





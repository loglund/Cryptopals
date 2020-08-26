# Cryptopals
Challenges from Cryptopals.com in Python

## Set 1 - Basics

- [x] [1. Hex to base-64 conversion](Basics/HexTo64.py):
- [x] [2. Fixed Xor operation](Basics/FixedXOR.py):
- Implentation of a equal-length XOR-function. Takes two equal length buffers as input and outputs their XOR result.
- [x] [3. Single Byte XOR Cipher](Basics/SingleByteXorCipher.py):
Code to decrypt and find the key of a Single-byte XOR cipher using statistics.

- First we infer the probabilities of the occurence of a specific letter in the english language in a dictionary (not divided by 100 yet)
This is used to compute a fitting quotient by counting the occurence of english letters in a given string (in ASCII)

- To break the single-byte XOR cipher, we then compute this fitting quotient of the encrypted message XOR'ed with all the possible characters in the ASCII table (the extended one 256 possible characters)

- The XOR'ed string with the minimum frequency is chosen to be the plaintext and the key is the character XOR'ed against the corresponding ciphertext

- [x] [4. Detect Single Character XOR](Basics/DetectSingleCharacterXOR.py):
Code to decrypt the txt-file (Basics/listOfPossibleCiphers.txt)
- First we read the file and convert the hex strings to bytes
- The code from (3) is then used to decrypt the strings

- [x] [5. Implement Repeating-Key XOR](Basics/RepeatingKeyXOR.py):
Code to encrypt plaintext by repeatedly XOR'ing a key with blocks of bytes. Will encrypt "Burning 'em, if you ain't quick and nimble / I go crazy when I hear a cymbal" with the key "ICE" to produce "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272 / a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f" 
- We XOR the first byte of the key with the first byte in the plaintext, then the second of the key with the second, etc. Finally we have used all characters in the key (k characters) and we start over by XOR'ing the first byte of the key to the (k+1)'th byte of the plaintext, and the process continues this way.

- [x] [6. Breaking Repeating-Key XOR](Basics/BreakingRepeatingKeyXOR.py):
Aimed to break the cipher that has encrypted the strings in (Basics/Challenge6.txt).
- First we infer a function to compute the Hamming distance of two strings (the number of positions in whichs their bits differ)
- We check in a range of possible key sizes (size_min, size_max) for the Hamming distance between the first key-size worth of bytes with the second key-size worth of bytes and divide this measure by the key-size. The minimal value of this over all checked key-sizes is chosen as the key-size (could choose multiple and test for further improvement)
- The ciphertext is then broken into blocks of size key-size and then transposed such that we get a list of key-size elements with lists of the first character of each block, the second character, etc.
- We then solve each block as if it was a single character XOR. If one chooses to use multiple candidates for key-sizes, one can then add a step that chooses which plaintext is the best solution by comparing the histogram of the different candidate keys.

- [x] [7. AES in ECB Mode](Basics/AESinECB.py):
Simple decryption of (Basics/AESCipher.txt) in ECB mode (128-bit) by knowing the key of the cipher "YELLOW SUBMARINE".

- [x] [8. Detect AES in ECB Mode](Basics/DetectAESinECB.py):
Code to detect if bytes have been encrypted with AES in ECB mode (128-bit).
- We count the repetition of blocks in the ciphertext. AES in ECB mode is deterministic so the same input yields the same ciphertext.
- If a block occurs more than once we return the bool True and False otherwise.
- We test it with (Basics/DetectECB.txt)

## Set 2 - Block Crypto (in progress)

- [x] [9. Implement PKCS7 Padding](BlockCrypto/PKCS7Padding.py):
Given a block size, we add padding to a string.
- If the length of the string is a multiple of the block size, we add a block of padding.
- If not we add padding to fill the last block.
- Implemented a PKCS7 stripping function to remove padding.

- [x] [10. Implement CBC Mode](BlockCrypto/CBCMode.py):
Code to both encrypt and decrypt an AES-ECB ciphertext in CBC mode.
- Infer a function to split our plaintext or ciphertext into blocks (or chunks) with block size 16.
- We XOR the plaintext chunks with the previous ciphertext chunks (first block is XOR'ed against an initialization vector (IV)) then AES-ECB encrypt the chunks.
- The decryption process first AES-ECB decrypts the ciphertext chunks and afterwards does the reverse process with the XOR'ing.
- Padded is added and stripped when needed.

-[x] [11. ECB/CBC Oracle](BlockCrypto/ECBCBCOracle.py):
An Oracle which encrypts plaintext in ECB or CBC with 50/50 probability. Key is randomly generated through the operating system.

-[x] [12. Byte-at-a-time ECB Decryption](ByteECBDecrypt.py):
Code to break the Oracle when it chooses ECB mode given a fixed random key (globally assigned) and appending a base-64 encoded string (presumed to the unknown) to the plaintext.
- Infered a function to decide the block size of the cipher (it is known to be 16, but generally it can be 16, 24 or 32) and a function to decide if the ciphertext is ECB encrypted.
- We feed the character "B" to the oracle repeatedly, first "B", then "BB", etc. 
- We then change the last character of the string to the next character and repeat until we guess correctly. We then target the next byte, then the next block and finally the whole ciphertext has been decrypted.








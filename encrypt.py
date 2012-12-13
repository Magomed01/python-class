# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:15:51 2012

Source: http://myw3b.net/blog/index.php/2011/01/vigenerecipher-3/
"""

ALPHABET   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PLAINTEXT  = 'HELLO'
KEY        = 'LEMON'
CIPHERTEXT = ''

# ENCRYPT
for i in range(len(PLAINTEXT)) :
    p = ALPHABET.index(PLAINTEXT[i])
    k = ALPHABET.index(KEY[i % len(KEY)])
    CIPHERTEXT += ALPHABET[(p + k) % len(ALPHABET)]
PLAINTEXT = ''
print "cipher text: ",CIPHERTEXT


# DECRYPT
for i in range(len(CIPHERTEXT)) :
    p = ALPHABET.index(CIPHERTEXT[i])
    k = ALPHABET.index(KEY[i % len(KEY)])
    if k - p < 0 :
        PLAINTEXT += ALPHABET[((p - k) + 26) % len(ALPHABET)]
    else :
        PLAINTEXT += ALPHABET[(p - k) % len(ALPHABET)]
 
print PLAINTEXT
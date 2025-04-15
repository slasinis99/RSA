import os
from random import randint, choice,seed
from sympy import isprime
from gcd import gcd, find_modular_inverse
import uuid

seed(uuid.getnode())

DIGIT_SIZE = 100

def big_prime() -> int:
    n = "1"
    while not isprime(int(n)):
        n = f"{randint(1,9)}"
        for _ in range(DIGIT_SIZE-2):
            n += f'{randint(0,9)}'
        n += f'{choice([1,3,7,9])}'
    return int(n)

def exp(b, e, m):
    if e < 0:
        b = 1 / b
        e = -e
    if e == 0:
        return 1
    y = 1
    while e > 1:
        if e % 2 == 1:
            y = (b * y) % m
            e = e - 1
        b = (b * b) % m
        e = e // 2
    return (b * y) % m

def pad(message, k):
    if len(message) > k - 11:
        raise ValueError("Message too long for the given key size (requires at least 11 bytes of padding)")
    ps_length = k - len(message) - 3
    ps = bytearray()
    while len(ps) < ps_length:
        r = os.urandom(1)
        if r != b'\x00':
            ps += r
    padded = b'\x00' + b'\x02' + bytes(ps) + b'\x00' + message
    return padded

def os2ip(byte_string):
    return int.from_bytes(byte_string, byteorder='big')

def i2osp(integer, length):
    return integer.to_bytes(length, byteorder='big')

def unpad(padded_bytes):
    delimiter_index = padded_bytes.index(b'\x00', 2)
    return padded_bytes[delimiter_index+1:]

class User():
    def __init__(self):
        p = big_prime()
        q = big_prime()
        self.n = p*q
        lambda_n = (p-1)*(q-1) // gcd(p-1, q-1, False)[0]
        self.e = 2**16+1
        self.d = find_modular_inverse(self.e, lambda_n, False)
    
    def public_key(self):
        return (self.n, self.e)
    
    def encrypt(self, n, e, s: str):
        plaintext_bytes = bytes(s, 'utf-8')
        padded_message = pad(plaintext_bytes, (n.bit_length() + 7) // 8)
        m = os2ip(padded_message)
        return exp(m, e, n)
    
    def decrypt(self, c):
        m = exp(c, self.d, self.n)
        padded_bytes = i2osp(m, (self.n.bit_length() + 7) // 8)
        plaintext_bytes = unpad(padded_bytes)
        return plaintext_bytes.decode('utf-8')
    

# bob = User()
# alice = User()

# # Bob is going to send Alice a message, so she needs bob's public key
# n, e = alice.public_key()

# #Bob now encrypts his message that is stored in the file: message.txt
# c = bob.encrypt(n, e, "Hello!")

# #Now Bob can send his encrypted message to Alice to Decode
# message = alice.decrypt(c)

# print(message)
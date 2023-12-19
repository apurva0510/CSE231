from proj04 import caesar_cipher_encryption

print("caesar_cipher_encryption('a',3,'abcdefgh'):",caesar_cipher_encryption('a',3,'abcdefgh'))
print("caesar_cipher_encryption('e',3,'2cdef78h'):", caesar_cipher_encryption('e',3,'2cdef78h')) 

assert caesar_cipher_encryption('a',3,'abcdefgh') == 'd'
assert caesar_cipher_encryption('e',3,'2cdef78h') == '8'

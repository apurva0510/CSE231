from proj04 import affine_cipher_encryption

print("affine_cipher_encryption('a',3,'abcdefgh'):",affine_cipher_encryption('a',3,'abcdefgh'))
print("affine_cipher_encryption('7',3,'2cdef78h'):", affine_cipher_encryption('7',3,'2cdef78h')) 

assert affine_cipher_encryption('a',3,'abcdefgh') == 'd'
assert affine_cipher_encryption('7',3,'2cdef78h') == 'd'

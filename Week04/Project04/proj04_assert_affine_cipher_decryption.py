from proj04 import affine_cipher_decryption

print("affine_cipher_decryption('d',3,'abcdefgh'):",affine_cipher_decryption('d',3,'abcdefgh'))
print("affine_cipher_decryption('d',3,'2cdef78h'):", affine_cipher_decryption('d',3,'2cdef78h')) 

assert affine_cipher_decryption('d',3,'abcdefgh') == 'a'
assert affine_cipher_decryption('d',3,'2cdef78h') == '7'

'''
CSE 231 Project 4

Algorithm
    define constants values
    define constant strings
    print welcome text
    input rotation
    while loop to keep the program running until user enters 'q'
        input command
        if command is 'e'
            input string to encrypt
            for loop to encrypt each character
                if character is alphanumeric then encrypt using affine cipher
                if character is punctuation then encrypt using caesar cipher
                else print error message and break
            else
                print plain text and cipher text
        if command is 'd'
            input string to decrypt
            for loop to decrypt each character
                if character is alphanumeric then decrypt using affine cipher
                if character is punctuation then decrypt using caesar cipher
                else print error message and break
            else
                print cipher text and plain text
        if command is 'q'
            break out of while loop
        else
            print error message and reinput command
'''
import math, string

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation

#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits


BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''


def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()


def multiplicative_inverse(A, M):
    '''
    Return the multiplicative inverse for A given M.
    Find it by trying possibilities until one is found.
    Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
    Returns:
        int: The multiplicative inverse of A modulo M.
    '''
    for x in range(M):
        if (A * x) % M == 1:
            return x


def check_co_prime(num, M):
    '''
    Check whether num is co-prime with M.
    Find it by equating GCD function from math library to 1.
    Args:
        num (int) and M (int): The numbers to check.
    Returns:
        bool: True if num is co-prime with M, False otherwise.
    '''
    if math.gcd(num, M) == 1:
        return True
    return False


def get_smallest_co_prime(M):
    '''
    Return the smallest number that is co-prime with M.
    Find it by trying possibilities until one is found.
    Args:
        M (int): The number whose smallest co-prime is to be found.
    Returns:
        int: The smallest number that is co-prime with M.
    '''
    for i in range(2, M):
        if check_co_prime(i, M):
            return i


def caesar_cipher_encryption(ch, N, alphabet):
    '''
    Return the encrypted character using caeser cipher encryption.
    Find it by using the formula (x + N) % M.
    Args:
        ch (str): The character to be encrypted.
        N (int): The number of rotations.
    alphabet (str): The string containing the alphabet.
    Returns:
        str: The encrypted character.
    '''
    x = 0

    M = len(alphabet)

    for i, char in enumerate(alphabet):
        if ch == char:
            x = i
            break

    E = (x + N) % M

    for i, char in enumerate(alphabet):
        if E == i:
            return char


def caesar_cipher_decryption(ch, N, alphabet):
    '''
    Return the decrypted character using caeser cipher decryption.
    Find it by using the formula (x - N) % M.
    Args:
        ch (str): The character to be decrypted.
        N (int): The number of rotations.
        alphabet (str): The string containing the alphabet.
    Returns:
        str: The decrypted character.
    '''
    x = 0

    M = len(alphabet)

    for i, char in enumerate(alphabet):
        if ch == char:
            x = i
            break

    D = (x - N) % M

    for i, char in enumerate(alphabet):
        if D == i:
            return char


def affine_cipher_encryption(ch, N, alphabet):
    '''
    Return the encrypted character using affine cipher encryption.
    Find it by using the formula (A * x + N) % M.
    Args:
        ch (str): The character to be encrypted.
        N (int): The number of rotations.
        alphabet (str): The string containing the alphabet.
    Returns:
        str: The encrypted character.
    '''
    x = 0

    M = len(alphabet)
    A = get_smallest_co_prime(M)

    for i, char in enumerate(alphabet):
        if ch == char:
            x = i
            break

    E = (A * x + N) % M
    
    for i, char in enumerate(alphabet):
        if E == i:
            return char


def affine_cipher_decryption(ch, N, alphabet):
    '''
    Return the decrypted character using affine cipher decryption.
    Find it by using the formula A_inv * (x - N) % M.
    Args:
        ch (str): The character to be decrypted.
        N (int): The number of rotations.
        alphabet (str): The string containing the alphabet.
    Returns:
        str: The decrypted character.
    '''
    x = 0

    M = len(alphabet)
    A = get_smallest_co_prime(M)
    A_inv = multiplicative_inverse(A, M)

    for i, char in enumerate(alphabet):
        if ch == char:
            x = i
            break

    D = A_inv * (x - N) % M

    for i, char in enumerate(alphabet):
        if D == i:
            return char


def main():
    print_banner(BANNER)

    N = input("Input a rotation (int): ")
    while True:
        try:
            N = int(N)
            break
        except ValueError:
            print("\nError; rotation must be an integer.")
            N = input("Input a rotation (int): ")

    N = int(N)

    command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
    command = command.lower()

    while command != 'q':
        if command == 'e':
            plain_text = input("\nInput a string to encrypt: ")
            plain_text = plain_text.lower()
            cipher_text = ''
            for ch in plain_text:
                if ch in ALPHA_NUM:
                    cipher_text += affine_cipher_encryption(ch, N, ALPHA_NUM)
                elif ch in PUNCTUATION:
                    cipher_text += caesar_cipher_encryption(ch, N, PUNCTUATION)
                else:
                    print("\nError with character: " + ch)
                    print("Cannot encrypt this string.")
                    break
            else:
                print("\nPlain text: " + plain_text)
                print("\nCipher text: " + cipher_text)

            command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")

        elif command == 'd':
            cipher_text = input("\nInput a string to decrypt: ")
            plain_text = ''
            for ch in cipher_text:
                if ch in ALPHA_NUM:
                    plain_text += affine_cipher_decryption(ch, N, ALPHA_NUM)
                elif ch in PUNCTUATION:
                    plain_text += caesar_cipher_decryption(ch, N, PUNCTUATION)
                else:
                    print("\nError with character: " + ch)
                    print("Cannot decrypt this string.")
                    break
            else:
                print("\nCipher text: " + cipher_text)
                print("\nPlain text: " + plain_text)
            
            command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")

        elif command == 'q':
            break

        else:
            print("\nCommand not recognized.")
            command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")




# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()
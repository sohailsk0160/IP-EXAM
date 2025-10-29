# Simple Hill Cipher (2x2 Matrix)

import numpy as np

# Convert letter to number (A=0, B=1,...)
def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

# Convert number back to letters
def numbers_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def encrypt(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'  # padding
    nums = text_to_numbers(text)
    encrypted = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2])
        result = np.dot(key_matrix, pair) % 26
        encrypted.extend(result)
    return numbers_to_text(encrypted)

def decrypt(cipher, key_matrix):
    # find modular inverse of determinant
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Key matrix is not invertible under mod 26!")

    # inverse of key matrix mod 26
    key_inv = (det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 26

    nums = text_to_numbers(cipher)
    decrypted = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2])
        result = np.dot(key_inv, pair) % 26
        decrypted.extend(result)
    return numbers_to_text(decrypted)

# ---------- MAIN ----------
print("=== Hill Cipher (2x2 Matrix) ===")
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()

text = input("Enter the text: ")
print("Enter 2x2 key matrix values (a b c d):")
a, b, c, d = map(int, input().split())
key_matrix = np.array([[a, b], [c, d]])

if choice == 'E':
    print("\nEncrypted Text:", encrypt(text, key_matrix))
elif choice == 'D':
    print("\nDecrypted Text:", decrypt(text, key_matrix))
else:
    print("Invalid choice! Please enter 'E' or 'D'.")

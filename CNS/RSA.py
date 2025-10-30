import math
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    return pow(e, -1, phi)

def generate_keys(p, q):
    if not (p > 1 and q > 1):
        raise ValueError("Both numbers must be prime.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e += 2 
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext_num):
    e, n = public_key
    ciphertext = pow(plaintext_num, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext_num = pow(ciphertext, d, n)
    return plaintext_num

# --- Main Program ---
p = 61
q = 53

print(f"Chosen primes: p={p}, q={q}")
public_key, private_key = generate_keys(p, q)
print(f"Public Key (e, n): {public_key}")
print(f"Private Key (d, n): {private_key}")
message = int(input("\nEnter a number to encrypt: "))
encrypted_message = encrypt(public_key, message)
print(f"Encrypted Message (Ciphertext): {encrypted_message}")
decrypted_message = decrypt(private_key, encrypted_message)
print(f"Decrypted Message (Plaintext): {decrypted_message}")

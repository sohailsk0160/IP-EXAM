# Simple Multiplicative Cipher

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # No inverse if not coprime with 26

def encrypt(text, key):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr(((ord(c) - base) * key) % 26 + base)
        else:
            result += c
    return result

def decrypt(text, key):
    inv = mod_inverse(key, 26)
    if inv is None:
        return "Invalid key! No modular inverse exists."
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr(((ord(c) - base) * inv) % 26 + base)
        else:
            result += c
    return result

# ---- MAIN PROGRAM ----
print("=== Multiplicative Cipher ===")
choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ").upper()
text = input("Enter the text: ")
key = int(input("Enter the key (must be coprime with 26): "))

if mod_inverse(key, 26) is None:
    print("❌ Invalid key! It has no modular inverse with 26.")
else:
    if choice == 'E':
        print("🔒 Encrypted Text:", encrypt(text, key))
    elif choice == 'D':
        print("🔓 Decrypted Text:", decrypt(text, key))
    else:
        print("Invalid choice! Use 'E' or 'D'.")

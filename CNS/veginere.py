# Simple Vigenere Cipher

def encrypt(text, key):
    result = ""
    key = key.lower()
    i = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % len(key)]) - ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            i += 1
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    key = key.lower()
    i = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % len(key)]) - ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            i += 1
        else:
            result += char
    return result

# ---------- MAIN ----------
print("=== Vigenere Cipher ===")
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
text = input("Enter the text: ")
key = input("Enter the key: ")

if choice == 'E':
    print("\nEncrypted Text:", encrypt(text, key))
elif choice == 'D':
    print("\nDecrypted Text:", decrypt(text, key))
else:
    print("Invalid choice! Please enter 'E' or 'D'.")

# Simple Additive (Caesar) Cipher

print("=== Additive (Caesar) Cipher ===")

# Get input from user
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
text = input("Enter the text: ")
key = int(input("Enter the key (0-25): "))

result = ""

for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        if choice == 'E':
            result += chr((ord(char) - base + key) % 26 + base)
        elif choice == 'D':
            result += chr((ord(char) - base - key) % 26 + base)
    else:
        result += char  # Keep spaces, numbers, and symbols same

# Show output
if choice == 'E':
    print(f"\nEncrypted Text: {result}")
elif choice == 'D':
    print(f"\nDecrypted Text: {result}")
else:
    print("Invalid choice! Please enter 'E' or 'D'.")

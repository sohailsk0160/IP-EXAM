# Simple Rail Fence Cipher

def encrypt(text, rails):
    fence = [''] * rails
    rail, step = 0, 1

    for char in text:
        fence[rail] += char
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1
    return ''.join(fence)

def decrypt(cipher, rails):
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    rail_len = [0] * rails
    idx_pattern = [pattern[i % len(pattern)] for i in range(len(cipher))]

    for i in idx_pattern:
        rail_len[i] += 1

    pos, rail_str = 0, []
    for r in rail_len:
        rail_str.append(list(cipher[pos:pos + r]))
        pos += r

    result, rail = '', 0
    for i in idx_pattern:
        result += rail_str[i].pop(0)
    return result

# ---------- MAIN ----------
print("=== Rail Fence Cipher ===")
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
text = input("Enter the text: ")
rails = int(input("Enter number of rails: "))

if choice == 'E':
    print("\nEncrypted Text:", encrypt(text.replace(" ", ""), rails))
elif choice == 'D':
    print("\nDecrypted Text:", decrypt(text, rails))
else:
    print("Invalid choice! Please enter 'E' or 'D'.")

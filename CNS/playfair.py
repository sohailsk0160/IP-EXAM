# Simple Playfair Cipher

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = ""
    for ch in key:
        if ch not in used and ch.isalpha():
            used += ch
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used += ch
    for i in range(5):
        matrix.append(list(used[i*5:(i+1)*5]))
    return matrix

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def prepare_text(text):
    text = text.upper().replace("J", "I")
    new_text = ""
    i = 0
    while i < len(text):
        a = text[i]
        if not a.isalpha():
            i += 1
            continue
        if i+1 < len(text):
            b = text[i+1]
            if not b.isalpha():
                i += 1
                continue
            if a == b:
                new_text += a + "X"
                i += 1
            else:
                new_text += a + b
                i += 2
        else:
            new_text += a + "X"
            i += 1
    return new_text

def encrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(text)
    cipher = ""
    for i in range(0, len(text), 2):
        cipher += encrypt_pair(matrix, text[i], text[i+1])
    return cipher

def decrypt(cipher, key):
    matrix = generate_key_matrix(key)
    text = ""
    for i in range(0, len(cipher), 2):
        text += decrypt_pair(matrix, cipher[i], cipher[i+1])
    return text

# --- MAIN PROGRAM ---
print("=== Playfair Cipher ===")
choice = input("Enter 'E' for Encrypt or 'D' for Decrypt: ").upper()
key = input("Enter the key: ")

if choice == "E":
    text = input("Enter the plaintext: ")
    print("Ciphertext:", encrypt(text, key))
elif choice == "D":
    text = input("Enter the ciphertext: ")
    print("Plaintext:", decrypt(text, key))
else:
    print("Invalid choice!")

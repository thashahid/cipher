def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

plaintext = "HELLO WORLD"
shift = 3
print("Plaintext:", plaintext)
print("Ciphertext:", caesar_cipher(plaintext, shift))

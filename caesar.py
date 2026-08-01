
def caesar_encrypt (text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char
        else:
            result += char 

    return result

def caesar_decrypt (text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Mesaj: ")
    shift = int(input("Shift: "))
    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("Criptat: ", encrypted)
    print("Decriptat: ", decrypted)

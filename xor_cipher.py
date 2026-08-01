def xor_encrypt (text, key):
    encrypted = bytearray()

    for i, byte in enumerate(text.encode("utf-8")):
        key_byte = key.encode("utf-8")[i % len(key.encode("utf-8"))]
        encrypted.append(byte ^ key_byte)

    return encrypted.hex()

def xor_decrypt(encrypted_hex, key):
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    decrypted = bytearray()
    key_bytes = key.encode("utf-8")

    for i, byte in enumerate(encrypted_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        decrypted.append(byte ^ key_byte)

    return decrypted.decode("utf-8")

if __name__ == "__main__":
    message = input("Mesaj: ")
    key = input("Key: ")
    if not key:
        print("Key nu poate fi gol.")
    else:
        encrypted = xor_encrypt(message, key)
        decrypted = xor_decrypt(encrypted, key)
        print("\nMesaj criptat (hex):", encrypted)
        print("Decriptat:", decrypted)


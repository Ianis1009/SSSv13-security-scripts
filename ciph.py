
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ciphertext_b64 = "0QMS8lOzbb3o3mO1IsI0XNPUCv7OojNcnBijUVxffh0="

keys = [
    "755f85c2723bb39381c7379a604160d8",
    "9dfc8dce7280fd49fc6e7bf0436ed325",
    "5f4dcc3b5aa765d61d8327deb882cf99",
]

ciphertext = base64.b64decode(ciphertext_b64)

for key_hex in keys:
    key = bytes.fromhex(key_hex)

    print("=" * 60)
    print(f"Trying key: {key_hex}")

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)

    print("Raw bytes :", plaintext)
    print("Hex       :", plaintext.hex())

    try:
        text = plaintext.decode("utf-8")
        print("UTF-8     :", text)
    except UnicodeDecodeError:
        print("UTF-8     : <invalid>")

    try:
        text = unpad(plaintext, 16).decode("utf-8")
        print("Unpadded  :", text)
    except Exception:
        print("Unpadded  : <invalid padding>")
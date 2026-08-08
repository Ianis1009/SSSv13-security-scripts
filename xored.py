
# key, input_file, output_file
key = 170
input_file = "xored"
output_file = "exe" # binary -> ./exe

with open(input_file, "rb") as f:
    data = f.read()

decoded = bytes(b ^ key for b in data)
with open(output_file, "wb") as f:
    f.write(decoded)

print(f"Decryption complete. Output saved to '{output_file}'")
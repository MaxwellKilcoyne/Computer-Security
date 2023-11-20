import hashlib

equal_sign_binary = "'='"

for i in range(10000000000):
    data = str(i).encode('latin-1')
    md5_hash = hashlib.md5(data).digest()
    
    strHash = md5_hash.decode('latin-1')

    if equal_sign_binary in strHash:
        print(f"Found MD5 hash with '=' in it: {i}")
        break
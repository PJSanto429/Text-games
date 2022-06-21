from cryptography.fernet import Fernet

def getKey():
    with open('key.key', 'rb') as file:
        key = file.read()
        file.close()
    return key

def encryptFile(fileName):
    key = getKey()
    fernet = Fernet(key)

    with open(f'players/{fileName}.json', 'rb') as f:
        data = f.read()
        f.close()

    encrypted = fernet.encrypt(data)
    with open(f'players/{fileName}.json', 'wb') as f:
       f.write(encrypted)
       f.close()

def decryptFile(fileName):
    key = getKey()
    fernet = Fernet(key)

    with open(f'players/{fileName}.json', 'r') as f:
        data = f.read()
        f.close()
    
    data_decoded = bytes(data, 'UTF-8')
    decrypted = fernet.decrypt(data_decoded)

    with open(f'players/{fileName}.json', 'wb') as outfile:
        outfile.write(decrypted)
        outfile.close()

def fileCryption(cryptionType, fileName):
    if cryptionType == 'decrypt':
        decryptFile(fileName)
    if cryptionType == 'encrypt':
        encryptFile(fileName)
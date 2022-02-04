from cryptography.fernet import Fernet
import os
import pathlib
from passlib.context import CryptContext
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

CURRENT_PATH = str(pathlib.Path(__file__).parent.absolute());
KEY_NAME = "secret.key"
PATH_KEY_NAME = CURRENT_PATH+'\\'+KEY_NAME

def generaChiave(pswd):
    password_provided = pswd  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)
    return key


def load_key(): 
    return open(PATH_KEY_NAME, "rb").read()

def encryptFile(dataBLOB):
    key = load_key()
    clear = dataBLOB.encode()
    f = Fernet(key)
    encrypted_clear = f.encrypt(clear)
    return encrypted_clear

def decryptFile(encDataBlob,pswd):
    key = generaChiave(pswd)
    f = Fernet(key)
    decrypted_clear = f.decrypt(encDataBlob)
    return decrypted_clear

if(os.path.isfile(CURRENT_PATH+"\\"+KEY_NAME)):
    print("Inserire messaggio da cryptare")
    clear = input()
    enc_clear = encryptFile(clear)
    print(enc_clear)
    print("Ora verrà decrittografato")
    print("Inserire MASTER password (solo se inserita corretta darà dati sensati):")
    pswd=input()
    if(generaChiave(pswd)==load_key()):
        print(decryptFile(enc_clear,pswd))
    else:
        print("La tua chiave è sbagliata")
else:
    print("Registrare una master password:")
    Mpass = input()
    chiave = generaChiave(Mpass)
    with open(PATH_KEY_NAME, "wb") as key_file:
        key_file.write(chiave)
    print("Inserire messaggio da cryptare")
    clear = input()
    enc_clear = encryptFile(clear)
    print(enc_clear)
    print("Ora verrà decrittografato")
    print("Inserire MASTER password (solo se inserita corretta darà dati sensati):")
    pswd=input()
    if(generaChiave(pswd)==load_key()):
        print(decryptFile(enc_clear,pswd))
    else:
        print("La tua chiave è sbagliata")



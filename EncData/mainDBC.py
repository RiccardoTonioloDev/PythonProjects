import sqlite3
import pathlib
import os.path
import os
import time
import base64
from PIL import Image
import io
from cryptography.fernet import Fernet
import pathlib
from passlib.context import CryptContext
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

DB_NAME = "Safe4Images.db"
PATH_DB = str(pathlib.Path(__file__).parent.absolute())+"\\"+DB_NAME

USER_SELECTION = 0

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
    clear = dataBLOB
    f = Fernet(key)
    encrypted_clear = f.encrypt(clear)
    return encrypted_clear

def decryptFile(encDataBlob,pswd):
    key = generaChiave(pswd)
    f = Fernet(key)
    decrypted_clear = f.decrypt(encDataBlob)
    return decrypted_clear

def convertToStringData(nomeFile):
    with open(nomeFile, 'rb') as fileInBinario:
        b64string = base64.b64encode(fileInBinario.read())
        #L'ERRORE è vvvvQUIvvvv, DEVO CAPIRE COME TRASFORMARE IN STRINGA UN BASE 64
        b64string = encryptFile(b64string)
        
    return b64string

def BinaryToFoto(nomeFile, fileString,pswd):
    imgData = base64.b64decode(decryptFile(fileString,pswd))
    with open(nomeFile, 'wb') as file:
        file.write(imgData)
        print("Foto estratta con successo! Nome file: "+nomeFile)

def insertBLOB(nomeFoto, fileString):
    if(os.path.isfile(PATH_DB)):
        conn = sqlite3.connect(PATH_DB)
        c = conn.cursor()
    else:
        conn = sqlite3.connect(PATH_DB)
        c = conn.cursor()
        c.execute('''CREATE TABLE immagini (chiave text PRIMARY KEY, FOTO_BLOB text NOT NULL)''')

    c.execute('''INSERT INTO immagini VALUES (?, ?)''',(nomeFoto, fileString))
    conn.commit()
    conn.close()

def extractBLOB(nomeFile,pswd):
    if(os.path.isfile(PATH_DB)):
        conn = sqlite3.connect(PATH_DB)
        c = conn.cursor()
        c.execute('''SELECT * FROM immagini WHERE chiave=?''', (nomeFile,))
        record = c.fetchone()
        conn.commit()
        BinaryToFoto(record[0],record[1],pswd)
        print("Foto scaricata in:")
        print(nomeFile)
    else:
        print("Per poter estrarre qualcosa dal database, bisogna prima crearlo!")

def deleteBLOB(nomeFile):
    conn = sqlite3.connect(PATH_DB)
    c = conn.cursor()
    c.execute('''DELETE FROM immagini WHERE chiave=?''', (nomeFile,))
    conn.commit()
    print("Eliminazione foto avvenuta con successo")

def rowExist(nomeFile):
    conn = sqlite3.connect(PATH_DB)
    c = conn.cursor()
    c.execute('''SELECT EXISTS(SELECT * FROM immagini WHERE chiave=?)''', (nomeFile, ))
    esiste = c.fetchone()
    conn.commit()
    return esiste


##############################################################################################
##################################PARTE PRINCIPALE############################################
##############################################################################################
if(not os.path.isfile(CURRENT_PATH+"\\"+KEY_NAME)):
    print("Registrare una master password da usare per criptare i files:")
    Mpass = input()
    chiave = generaChiave(Mpass)
    with open(PATH_KEY_NAME, "wb") as key_file:
        key_file.write(chiave)
while(USER_SELECTION!=3):
    print("---------------Safe4Images---------------")
    print("Cosa desideri fare?")
    print("[0] Inserire una foto")
    print("[1] Scaricare una foto")
    print("[2] Eliminare una foto")
    print("[3] Chiudere")
    print("-----------------------------------------")
    USER_SELECTION = input()
    if(USER_SELECTION.isnumeric()):
        USER_SELECTION = int(USER_SELECTION)
    else:
        USER_SELECTION = 5
    if(USER_SELECTION==0):
        print(":::::::::::::::::::::::::::::::::::::::::::")
        print(":::::::::::::Caricare una foto:::::::::::::")
        print("Inserire il nome del percorso completo per la foto o il file da caricare")
        PATH_FILE = input()
        if(os.path.isfile(PATH_FILE)):
            print(PATH_DB)
            if(os.path.isfile(PATH_DB)):
                if(rowExist(PATH_FILE)[0]!=0):
                    print("File con lo stesso nome già presente nell'archivio")
                else:
                    insertBLOB(PATH_FILE,convertToStringData(PATH_FILE))
            else:
                insertBLOB(PATH_FILE,convertToStringData(PATH_FILE))
        else:
            print("Per piacere immettere il percorso di un file realmente esistente")
        print(":::::::::::::::::::::::::::::::::::::::::::")
    elif(USER_SELECTION==1):
        print("::::::::::::Scaricare una foto:::::::::::::")
        print("Inserire il nome del percorso completo che identificava il tuo file al momento del caricamento")
        PATH_FILE = input()
        if(rowExist(PATH_FILE)[0]==0):
            print("File cercato non presente nel database")
        else:
            print("Inserire chiave per decrittografazione:")
            Mpass2=input()
            if(generaChiave(Mpass2)==load_key()):
                extractBLOB(PATH_FILE,Mpass2)
            else:
                print("Mi dispiace ma la chiave che hai usato non funziona")
        print(":::::::::::::::::::::::::::::::::::::::::::")
    elif(USER_SELECTION==2):
        print("::::::::::::Eliminare una foto:::::::::::::")
        print("Inserire il nome del percorso completo che identificava il tuo file al momento del caricamento")
        PATH_FILE = input()
        deleteBLOB(PATH_FILE)
        print(":::::::::::::::::::::::::::::::::::::::::::")
    elif(USER_SELECTION==3):
        os.system("cls")
        print('Sto chiudendo')
        time.sleep(1)
        os.system("cls")
        print('Sto chiudendo.')
        time.sleep(1)
        os.system("cls")
        print('Sto chiudendo..')
        time.sleep(1)
        os.system("cls")
        print('Sto chiudendo...')
        time.sleep(1)
        os.system("cls")
    else:
        print(USER_SELECTION)
        print("Per favore scegliere un valore compreso tra 0 e 2")
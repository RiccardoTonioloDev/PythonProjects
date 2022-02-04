import sqlite3
import pathlib
import os.path
import os
import time
import base64
from PIL import Image
import io

DB_NAME = "Safe4Images.db"
PATH_DB = str(pathlib.Path(__file__).parent.absolute())+"\\"+DB_NAME

USER_SELECTION = 0

def convertToStringData(nomeFile):
    with open(nomeFile, 'rb') as fileInBinario:
        b64string = base64.b64encode(fileInBinario.read())
        blobFile = fileInBinario.read()
        
    return b64string

def BinaryToFoto(nomeFile, fileString):
    imgData = base64.b64decode(fileString)
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

def extractBLOB(nomeFile):
    if(os.path.isfile(PATH_DB)):
        conn = sqlite3.connect(PATH_DB)
        c = conn.cursor()
        c.execute('''SELECT * FROM immagini WHERE chiave=?''', (nomeFile,))
        record = c.fetchone()
        conn.commit()
        BinaryToFoto(record[0],record[1])
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
            extractBLOB(PATH_FILE)
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
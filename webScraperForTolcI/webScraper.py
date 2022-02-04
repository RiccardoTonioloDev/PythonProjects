from bs4 import BeautifulSoup
import requests
import time


correct_city = 2
counter = 0
found = 0
print('Inserisci il nome della città da cercare: ')
ctts=input()
print('-------------------------------------------')
while 1<2:
    html_text = requests.get('https://tolc.cisiaonline.it/calendario.php?tolc=ingegneria').text
    soup = BeautifulSoup(html_text, 'lxml')
    tabella = soup.find_all('td')
    for linea in tabella:
        if(counter==correct_city and linea.text==ctts):
            found = 1
            correct_city += 9
            counter += 1 
        else:
            if(counter==correct_city):
                correct_city += 9
            counter += 1 
    if(found!=0):
        print('!!!-------------------------------------------!!!')
        print('RISULTATO TROVATO')
        print('!!!-------------------------------------------!!!')
    else:
        print('Non trovato, sto ancora cercando!')
    time.sleep(15)
    
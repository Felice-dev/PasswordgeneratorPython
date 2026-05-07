import random
import string

def setLength():
    """Chiediamo all'utente di inserire la lunghezza della password, gestendo
    la casistica in cui l'input sia inferiore alla lunghezza minima o non 
    sia un numero intero"""
    while True:
        risposta = input("Inserisci il numero di lunghezza della password: ")
        try:
            """Gestiamo le eccezioni assicurandoci che l'utente inserisca
            un numero intero e che sia maggiore di 5"""
            length = int(risposta)
            if length <= 5:
                print("La lunghezza della password deve essere maggiore di 5. Riprova.")
            else:
                """Arrivando qui, l'input inserito è valido e possiamo uscire 
                dalla funzione senza problemi"""
                return length
        except ValueError:
            """Qui gestiamo la casistica dell'errore e riprendiamo l'iterazione
            del ciclo while"""
            print("Input non valido. Per favore, inserisci un numero intero.")

def generatePassword(length):
    """Generiamo una password casuale, utilizzando una sintassi più compatta
    e rapida rispetto a quella usata nel generatore in C++"""
    caratteri_validi = string.ascii_letters + string.digits + string.punctuation
    """Creiamo una stringa caratteri_validi che conterrà tutte le lettere, i
    numeri e i caratteri speciali, concatenandoli tra di loro nella stringa
    che utilizzeremo come base per la generazione della password"""
    return "".join(random.choice(caratteri_validi) for _ in range(length))
    """RItorna direttamente la password generata, unendo tra di loro ogni
    simbolo estratto in un unica stringa lunga quanto il valore di 
    length inserito dall'utente"""

def valutePassword(password, length):
    """Valutiamo la robustezza della password in base a diversi criteri, gli
    stessi presenti nell'altro calcolatore di password, restituendo il livello
    di sicurezza su una scala dove il massimo è 5 e il minimo è 0"""
    level_check = 0
    has_upper = False
    has_number = False
    has_special = False
    repeated = False
    """Definiamo le varie variabili che risponderanno ai diversi criteri"""

    if length>=10:
        level_check += 1
    """Controlliamo la lunghezza della password"""
    for char in password:
        if char.isupper():
            has_upper = True
        """Controlliamo se sono presenti lettere maiuscole, aggiornando la variabile
        has_upper di conseguenza"""
        if char.isdigit():
            has_number = True
        """Controlliamo se sono presenti numeri, aggiornando la variabile 
        has_number di conseguenza"""
        if char in string.punctuation:
            has_special = True
        """Controlliamo se sono presenti caratteri speciali, aggiornando la
        variabile has_special di conseguenza"""
    for i in range(length-1):
        if password[i] == password[i+1]:
            repeated = True
            break
        """Controlliamo se sono presenti caratteri ripetuti consecutivamente,
        aggiornando la variabile repeated di conseguenza"""

    if has_upper:
        level_check += 1
    if has_number:
        level_check += 1
    if has_special:
        level_check += 1
    if not repeated:
        level_check += 1
    """Aggiorniamo il livello di sicurezza in base ai criteri soddisfatti"""
    return level_check
    """Restituiamo il livello di sicurezza calcolato"""
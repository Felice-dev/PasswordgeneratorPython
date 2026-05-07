# Generatore di Password Sicure (Python)

Una versione in Python del generatore di password modulare. 
Questo progetto dimostra l'implementazione di logiche di validazione, generazione casuale e calcolo della robustezza utilizzando la sintassi pulita e le librerie standard di Python.

## Funzionalità
- **Generazione Casuale**: Sfrutta il modulo `random` e `string` per creare password con lettere, numeri e simboli.
- **Validazione dell'Input**: Gestione sicura degli errori tramite blocchi `try-except` per prevenire crash se l'utente inserisce caratteri non validi.
- **Valutazione della Sicurezza**: Analizza la password (da 0 a 5) verificando:
  - Lunghezza minima (10+ caratteri)
  - Presenza di maiuscole e numeri
  - Presenza di caratteri speciali
  - Assenza di caratteri ripetuti consecutivamente

## Struttura del Codice
- `main.py`: Punto di ingresso del programma, gestisce l'interfaccia utente tramite console usando le *f-string*.
- `password_utils.py`: Modulo contenente il "motore" del programma (funzioni di input, generazione e valutazione).

## Come usarlo
Assicurati di avere **Python 3** installato sul tuo computer.

1. Clona il repository:
   ```bash
   git clone [https://github.com/TuoNomeUtente/PasswordGenerator-Python.git](https://github.com/TuoNomeUtente/PasswordGenerator-Python.git)

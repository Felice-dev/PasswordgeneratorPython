from password_utils import setLength, generatePassword, valutePassword

def main():
    print(" Benvenuto nel generatore di password in Python!")

    """Chiediamo i parametri con i quali creeremo la password casuale"""
    length = setLength()
    """Generiamo la password casuale"""
    password = generatePassword(length)
    print(f"Password generata: {password}")

    """Valutiamo la robustezza della password generata"""
    security_level = valutePassword(password, length)
    print(f"Livello di sicurezza della password: {security_level}/5")

if __name__ == "__main__":
    main()
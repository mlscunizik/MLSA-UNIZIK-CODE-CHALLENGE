def Encrypt_Decrypt(mode):

    # The string to be encrypted/decrypted:
    if mode == 'encrypt':
        message = input('''Enter message to be encrypted
>> ''').strip()
    elif mode == 'decrypt':
        message = input('''Enter message to be Decrypted
>> ''').strip()

    # The encryption/decryption key:
    #this was gotten by analysing the differences between the encrypted messages and the real messages.
    key = 3

    # Every possible symbol that can be encrypted:
    SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'

    # Stores the encrypted/decrypted form of the message:
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol.lower() in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol.lower())

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            if symbol.isupper():
                translated = translated + (SYMBOLS[translatedIndex]).upper()
            elif symbol.islower():
                translated = translated + (SYMBOLS[translatedIndex]).lower()
   
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Output the translated string:
    return(translated)

def main():
    print ('''
    -------------------------------
    | Written by Mr King Austin   |
    ===============================''')

    while True:
        user = input('''
Select the Challenge to Run
ENTER [1] to 'Encrypt'
ENTER [2] to run "Decrypt"
ENTER [q] to QUIT
>> ''').strip()
        if not user.isnumeric():
            exit("Have a nice day")
        if user == '1':
            
            print('>> ', Encrypt_Decrypt('encrypt'))
        elif user =='2':
             print('>> ', Encrypt_Decrypt('decrypt'))

        else:
            print(" ==> ENTER A VALID NUMERIC INPUT ")

        continue

if __name__ == '__main__':
    main()


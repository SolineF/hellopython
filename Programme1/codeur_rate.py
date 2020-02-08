#! /usr/local/bin/python3

message_code = input("Saisissez un code en majuscule.")
#message_code = ""

#for lettre in message:
    #numero_caractere = ord(lettre)
    #numero_caractere_code = numero_caractere + 12
    #if(numero_caractere_code > ord("Z")):
        #numero_caractere_code = numero_caractere_code - 26
    #caractere_code = chr(numero_caractere_code)
    #message_code = message_code + caractere_code
#print(message_code)

message_decode = ""
for lettre in message_code:
    numero_caractere_code = ord(lettre)
    numero_caractere_decode = numero_caractere_code - 12
    if(numero_caractere_decode < ord("A")):
        numero_caractere_decode = numero_caractere_decode + 26
    caractere_decode = chr(numero_caractere_decode)
    message_decode = message_decode + caractere_decode
print(message_decode)
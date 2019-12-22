#! /usr/local/bin/python3

message_code = input("Saisissez un code en majuscule.")
message_decode = ""
for lettre in message_code:
    numero_caractere_code = ord(lettre)
    numero_caractere_decode = numero_caractere_code - 12
    if(numero_caractere_decode < ord("A")):
        numero_caractere_decode = numero_caractere_decode + 26
    caractere_decode = chr(numero_caractere_decode)
    message_decode = message_decode + caractere_decode
print(message_decode)
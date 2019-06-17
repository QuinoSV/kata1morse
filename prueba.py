letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?"!'
simbolos = ['·—','—···','—·—·','————','—··','·','··—·','——·','····','··','·———','—·—','·—··','——','—·','——·——','———','·——·','——·—','·—·','···','—','··—','···—','·——','—··—','—·——','——··','—————','·————','··———','···——','····—','·····','—····','——···','———··','————·','·—·—·—','—·—·——','··——··','·—··—·','——··——']

cadena = "Hola, Mundo".upper()

for letra in cadena:
    posicion = 0
    while posicion < len(letras):
        l = letras[posicion]
        if l == letra:
            break
        posicion +=1
    if posicion == len(letras):
        print("No encontrado")
    else:
        #Obtener simbolo morse de posicion
        print("{}:  {}".format(letra, simbolos[posicion]))

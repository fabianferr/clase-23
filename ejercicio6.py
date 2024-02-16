frases = []
while True:
    frase = input("Introduce una frase (o 'salir' para terminar): ")
    if frase.lower() == 'salir':
        break
    frases.append(frase)
print("Número de frases:", len(frases))

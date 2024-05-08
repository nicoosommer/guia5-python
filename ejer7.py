def palabras(frase):
    palabras=1
    for i in frase:
        if i==" ":
            palabras+=1
    return palabras
f=input("Ingrese uina frase: ")
print("La frase tiene ",palabras(f)," palabras")
def mayor(edad):
    if edad>=18:
        txt= "Edad mayor a 18"
    else:
        txt="Edad menor a 18"
    return txt 
edad=int(input("Ingrese su edad: "))
print(mayor(edad))
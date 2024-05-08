def validar(nombre,apellido):
    num=["0","1","2","3","4","5","6","7","8","9"]
    valid=0
    for i in nombre:
        if i in num:
            valid+=1
    for i in apellido:
        if i in num:
            valid+=1
    if valid==0:
        print("El nombre y apellido son correctos. ")
    else: 
        print("No son correctos los datos ingresados.")
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
validar(nombre,apellido)
    
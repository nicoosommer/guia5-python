def calculadora(op,num1,num2):
    if op==1:
        return num1+num2
    elif op==2:
        return num1-num2
    elif op==3:
        return num1*num2
    elif op==4:
        return num1/num2
    else:
        return "Ingreso una operacion incorrecta"
num1=float(input("Ingrese un num: "))
num2=float(input("Ingrese otro num: "))
op=int(input("Ingrese 1 para suma, 2 para resta, 3 para multiplicacion y 4 para divison: "))
print("El resultado es: ",calculadora(op,num1,num2))
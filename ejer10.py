def valor(precio):
    p=precio/1.21
    iva=precio-p
    txt=f"El valor del producto original es {p} y el iva del 21% es de {iva}."
    return txt
precio=int(input("Ingrese el precio de un articulo: "))
print(valor(precio))
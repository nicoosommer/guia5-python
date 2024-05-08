def saludo(hora):
    if hora>=6 and hora <=12:
        txt="Buenos dias"
    elif hora>12 and hora<=19:
        txt="Buenas tardes"
    else:
        txt="Buenas noches"
    return txt
hora=float(input("Ingrese que hora es"))
print(saludo(hora))
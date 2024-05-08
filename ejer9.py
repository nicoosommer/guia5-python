def distancia(x2,y2):
    x1=3
    y1=5
    distancia=((x1-x2)**2+(y1-y2)**2)**.5
    return distancia
x2=int(input("Ingrese el valor x de la coordenada: "))
y2=int(input("Ingrese el valor y de la coordenada: "))
print(f"Ustede se encuentra a {distancia(x2,y2)}km")
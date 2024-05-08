import random
import string
def contra():
    contraseña=""
    for _ in range(3):
        contraseña+=random.choice(string.ascii_lowercase)
    contraseña+=str(random.randint(10,99))
    for i in range(3):
        contraseña+=random.choice(string.ascii_uppercase)
    return contraseña
print("Su contraseña es: ",contra())
import random
nombres=["Nico","Jose","Facu","Hernan","marcelo","Ricardo","Alicia","Marina","Sofia","Morena","Ramon", "Sergio","Ernesto"]
apellidos=["Sommer","Riveros","Gutierrez","Torres","Salomon","Mandirlles","Villanueva","Manislla","Prados","Santini","Bujedo"]
edad=[]
peso=[]
for i in range(20) :
    edad.append(random.randint(10,80))
for i in range(20):
    peso.append(random.randint(50,110))
print(edad)
print(peso)
def listado():
    lista=[]
    for i in range(10):
        txt=""
        txt+=f"{random.choice(apellidos)} {random.choice(nombres)}.{str(random.choice(edad))} años, {str(random.choice(peso))} kg"
        lista.append(txt)
    lista.sort()
    return lista
print(listado())
import random
def grilla():
    nums=[]
    for i in range(10):
        num=random.randint(1,1000)
        nums.append(num)
    return nums
print("La grilla de 10 numeros random es: ",grilla())
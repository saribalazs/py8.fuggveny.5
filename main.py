'''
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! 
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. 
A program írja ki, hogy melyik volt a megadott legkisebb szám!
'''
def legkisebb():
    n = sum(lista)
    for i in lista:
        if i < n:
            n = i
    return n

lista = []
while True:
    num = int(input("Kérem adjon meg egy számot!"))
    if num < 0:
        break
    else:
        lista.append(num)

print(lista)
print(legkisebb())
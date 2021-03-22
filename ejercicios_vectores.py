# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:04:13 2021
"""

def sumatoria(vector):
    sumatoria = 0
    for i in vector:
        sumatoria = sumatoria + i
    return sumatoria

def productoria(vector):
    productoria = 1
    for i in vector:
        productoria = productoria * i
    return productoria

def mayor(vector):
    mayor = vector[0]
    for i in vector:
        if i > mayor:
            mayor = i
    return mayor

def menor(vector):
    menor = vector[0]
    for i in vector:
        if i < menor:
            menor = i
    return menor

def pares(vector):
    pares = 0
    for i in vector:
        if i % 2 == 0:
            pares = pares + 1
    return pares

def impares(vector):
    impares = 0
    for i in vector:
        if i % 2 == 1:
            impares = impares + 1
    return impares


def esPrimo(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return False
        return True
    else:
        return False

def primos(vector):
    primos = 0
    for i in vector:
        if esPrimo(i):
            primos = primos + 1
    return primos

def suma(v,v1):
    if (len(v) == len(v1)):
        return [x+y for x, y in zip(v,v1)]
    else:
        return "Para realizar una suma o una resta ambos vectores deben tener la misma longitud"

def resta(v,v1):
    if (len(v) == len(v1)):
        return [x-y for x, y in zip(v,v1)]
    else:
        return "Para realizar una suma o una resta ambos vectores deben tener la misma longitud"

def repeticiones(vector):
    repeticiones = {x:vector.count(x) for x in vector}
    maximo = max(repeticiones.values())
    numeros = []
    for i in vector:
        if repeticiones[i] == maximo:
            numeros.append(i)
    return f"Él(Los) número(s) que más se repite(n) es(son): {numeros}"

def dividir_partes(vector):
    if len(vector) % 2 == 0:
        parte1 = vector[0:int(len(vector)/2)]
        parte2 = vector[int(len(vector)/2):]
        print(f"Sumatoria parte 1: {sumatoria(parte1)}, Productoria parte 2: {productoria(parte2)}")
    else:
        return "No se puede realizar el proceso dado que su longitud no es par"

def simetrico(vector):
    if len(vector) % 2 == 0:
        parte1 = vector[0:int(len(vector)/2)]
        # La sintaxis del operador es inicio:fin:paso (si se pone -1 en paso reversa la lista)
        parte2 = vector[int(len(vector)/2):][::-1]
        return parte1 == parte2
    else:
        return "Para que el vector sea simétrico debe tener longitud par"
    
def union(A,B):
    return list(set(A+B))

def interseccion(A,B):
    return [x for x in A if x in B]

def diferencia_A_B(A,B):
    lista1 = {x:A.count(x) for x in A}
    lista2 = {x:B.count(x) for x in B}
    resultado = []
    for i in lista1.keys():
        if i in lista2.keys():
            lista1[i] = lista1[i] - lista2[i]
        for x in range(lista1[i]):
            resultado.append(i)
    return resultado
    

def diferencia_B_A(A,B):
    lista1 = {x:B.count(x) for x in B}
    lista2 = {x:A.count(x) for x in A}
    resultado = []
    for i in lista1.keys():
        if i in lista2.keys():
            lista1[i] = lista1[i] - lista2[i]
        for x in range(lista1[i]):
            resultado.append(i)
    return resultado

def punto1(vector):
    print(f"Sumatoria: {sumatoria(vector)}")
    print(f"Productoria: {productoria(vector)}")
    print(f"Mayor elemento: {mayor(vector)}")
    print(f"Menor elemento: {menor(vector)}")

def punto2(vector):
    print(f"Pares: {pares(vector)}")
    print(f"Impares: {impares(vector)}")
    print(f"Primos: {primos(vector)}")

def punto3(v,v1):
    print(f"Suma: {suma(v,v1)}")
    print(f"Resta: {resta(v, v1)}")

def punto4(vector):
    print(f"{repeticiones(vector)}")

def punto5(vector):
    dividir_partes(vector)
    
def punto6(vector):
    if simetrico(vector):
        print(f"El vector {vector} es simétrico")
    else:
        print(f"El vector {vector} no es simétrico")

def punto7(A,B):
    print(f"Unión: {union(A,B)}")
    print(f"Intersección: {interseccion(A,B)}")
    print(f"Diferencia(A-B): {diferencia_A_B(A,B)}")
    print(f"Diferencia(B-A): {diferencia_B_A(A,B)}")

#Pruebas
A = [1, 2, 3, 4]
B = [1, 1, 2, 3, 3, 3, 4, 4, 4, 5]
punto1(A)
punto2(A)
punto3(A,A)
punto4(A)
punto5(A)
punto6(A)
punto7(A,B)
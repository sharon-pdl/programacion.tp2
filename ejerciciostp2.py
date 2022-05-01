"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes: (Escriba aqui suz nombrez)

Práctico 3: Listas y cadenas de caracteres
"""

# 1 Escribir una función sum() que sume todos los números de una lista. 
"""    
def sum(a:[int])->int:
    pass
assert sum([1,2,3,4]) == 10
assert sum([1,2,3,4]) != 30
"""
##############

def sum(a:[int])->int:
resultado = 0
for i in a:
    resultado = i + resultado
return resultado

assert sum([1,2,3,4]) == 10
assert sum([1,2,3,4]) != 30

# 2 Escribir una función mul() que multiplique todos los números de una lista.
"""def mul(a:[int])->int:
    pass
assert mul([1,2,3,4]) == 24
"""
def mul(a:[int])->int:
resultado = 1
  for i in a:
    resultado = i * resultado
return resultado

assert mul([1,2,3,4]) == 24

# 3 Sin usar la funcion de lista count implementar la funcion que cuenta la cantidad de veces que aparece une elemento en una lista.
""""
def contar(l:list,a:elem)->int:
    pass
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2
"""

def contar(l:list,a: int)->int:
contador = 0
for i in l:
    if a == i:
      contador = contador + 1
return contador



assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2
# 4 Definir una función longitud() que calcule la longitud de una lista o una cadena dada. (Python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).
""""
def longitud(a:list)->int:
    pass
assert longitud([1,2,3,4]) == 4
assert longitud([]) == 0
""""

def longitud(a:list)->int:
contador = 0
  for i in a:
    contador+=1
return contador

assert longitud([1,2,3,4]) == 4
assert longitud([]) == 0

# 5 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
""""
def superposicion(a:List,b:List)->bool:
    pass
assert superposicion([1,2,3],[2,4,8]) == True #(2 se esta en las 2 listas)
assert superposicion([1,3,5],[2,4,6]) == False #(no hay elementos comunes)
"""

def superposicion(a:list,b:list)-> bool:
contador = False
for i in a:
    for j in b:
      if i == j:
        contador = True
return contador

assert superposicion([1,2,3],[2,4,8]) == True #(2 se esta en las 2 listas)
assert superposicion([1,3,5],[2,4,6]) == False #(no hay elementos comunes)


# 6 Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
def remover_dup(l:list)->list:
    pass
assert remover_dup([1,5,6,7,2,3,4,1,2,5]) == [1, 5, 6, 7, 2, 3, 4]


# 7 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def esvocal(c:str)->bool:
    pass
assert es_vocal ("f") == False
assert es_vocal ("a") == True
assert es_vocal ("ala") == False
assert es_vocal ("aa") == False

# 8 Hacer una función que intercambie los caracteres indice i,j de un string, si los inices son mayores al largo del string no deberia hacer nada
def intercambiar_dos(s:str,i:int,j:int)->str:
    pass
intercambiar_dos("hola mundo",0,5) == "mola hundo"
intercambiar_dos("hola mundo",0,20) == "hola mundo"

# 9 Hacer una función que de vuelta las palabras sin usar la función reverse.
def dar_vuelta(s:str)-> str:
    pass
assert dar_vuelta("hola") == "aloh"

# 10 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)
def es_palindromo(s:str)->bool:
    pass
assert es_palindromo ("radar") == True
assert es_palindromo ("rada") == False

# 11 Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
def generar_n_caracteres(n:int,c:str)->str:
    pass
assert generar_n_caracteres(5, "x") == "xxxxx"
assert generar_n_caracteres(4, "x") != "xxxxx"
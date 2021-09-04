# Variables I/O

## Este es un subtitulo

Con shift + Enter se ejecuta la celda

Escribo simplemente un comentario, aca el profe explico que las celdas bla bla....

suma = 5 + 8

suma

suma_backup = suma

print(suma)

suma + 1

suma = 0

print(suma)

print(suma_backup)





a = 5
b = 8

c = a + b





print(c)

c

# Funciones básicas

print(a+b)

print(a**3)

a//2  # Division entera

a%2  # modulo, resto de la division

a/2

raiz_9 = 9**0.5
raiz_9

# Funciones predefinidas

Machete:
    
    nombreFuncion(argumento1, argumento2... [argunmentoN])





flotante = 3.1415141592653589
round ( flotante , 5)

a = 1
b = 2

round(flotante, 2)

round(flotante)





flotante

flotante = round(flotante, 4)

flotante

nombre = 'Juan'
edad = 43

print(nombre, edad)
print(nombre)

# Case Sensitive

nombre = "Juan"
Nombre = "Ignacio"

print(Nombre)

flotante = 3.1415141592653589
flotante = round(flotante, 3)
flotante

print(flotante)



# Palabras Reservadas

help('keywords')





# Ayuda de funciones

print?

help(print)

a = 5
b = 10
c = "juan"

print(a,b,c, sep='---')



print(a, b,c)

print(a, end='\n******\n')

print(b,c, sep=',')













# Tipos de Variables

a = 1,000,000
a

pi = 3,141592

pi

# TypeError

a , b = 5, 8

## Entero

a = 5
type(a)

print(5)

## Flotante

a = 0.1
type(a)

round(3.14)

type(a)

## Complejo?

complejo = (-4) **0.5
complejo

type(complejo)



a = 0.1
b = 0.2
a,b

res = a+b
res

## Booleanos

a = True
b = False

a,b

type(a)

## No-Numéricos => Strings

a = 33
a

print(type(a))

a = '33'
a

print(type(a))

# Pasar de un tipo a otro

a = "33"
a_int = int(a)

print(type(a), type(a_int))
a, a_int

# Input por teclado

edad = 40

print(edad)

edad = input('Ingresa tu edad: ')


print(type(edad))

edad

edad = input('Ingresa tu edad: ')
edadNumero = float(edad)

edad

edadNumero

int('43,5')

int(float('43.5'))







edad = input('Ingresa tu edad: ')
edadNumero = float(edad)

print(edad, type(edad))
print(edadNumero, type(edadNumero))

edad = input('Ingresa tu edad: ')
edadNumero = edad

print(edad, type(edad))
print(edadNumero, type(edadNumero))

variable = 43
type(variable)

variable = 43.0
type(variable)

variable = '43'
type(variable)

# Strings

a = '55'
b = "10"

(a+b)

b*5

nombre = 'juan'

nombre.upper()

stringLargo =  '''
                Hola gente:
                
                
                
                
                
                Así puedo escribir muchas lineas

                chau gente
                '''

print(stringLargo)

# Format Strings

a = 5

print('El numero a vale:', a)

a =  5.4546546546516

print(f'El numero a vale {a}')

a =  5.4546546546516

print(f'El numero a vale {round(a,3)}')

a =  5.4546546546516

print(f'El numero a vale {a:.3f}')

nombre = 'Juan'
accionPreferida = 'COME'
variacion = 0.0125

string  = F'Hola {nombre}, tu accion preferida {accionPreferida} hoy varíó {variacion:.2%}'
string







# Funciones de strings

nombre = 'Juan'

print(type(nombre), nombre)

dir(nombre)

nombre es el objeto (en este caso es un objeto del tipo string)


upper es el metodo



help es la instruccion que me devuelve la ayuda de: 

help(nombre.upper)

nombre.upper()



help(nombre.find)



frase = 'yo me llamo juan pablo'

frase.find('Nacho')

frase.replace(" ", "--")

frase

frase.title()

frase.split(' ')





# Librerias

import math

math.pi

math.e

math.log(100, 10)

help(math.log)

math.log(math.e)# IndicadoreTecnicos

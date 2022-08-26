"""
El algoritmo que voy a crear principalmente va a ayudar a los restaurantes y pequeñas tiendas, se trata de crear un algoritmo, el cual al inicio se despliegue un
menú con las opciones que el restaurante o la pequeña tienda tengan, una vez que el usuario ha leído todas las opciones, mediante números va escogiendo lo que 
quiere pedir y el algoritmo le calcula y al final le sale la cuenta. Además, al final, se podría calcular la propina que se le va a dar al mesero y se puede 
calcular el servicio que él/ella le da.

Para definir el tiempo final, hay que poner un if y el programa tiene que ver si el tiempo es mayor o no.

Definir variables 


1. Desplegar el menú

2. Crear una variable “comida”

3. Mientras que “comida” sea mayor que 0

  3.1. Pedirle al usuario lo que va a comer 
  3.2. Volver al paso 3 
4. Sumar todas las opciones que el usuario ha escogido (Operaciones)

5. Mostrar el monto final

6. Cuando ya terminé de comer/pagar, preguntar al usuario si quiere agregar propina

7. Si el usuario quiere agregar propina

    7.1 Pedirle que digite el monto de propina 
8. Pedirle al usuario que califique la atención

9. Si el usuario quiere calificar 
   9.1. Pedirle al usuario que introduzca la satisfacción

"""
# La variable "costo", es lo que va a tener cada entrada, plato fuerte, guarnicion, 
costo = 0
costo_final = 0
propina = 0
costo_postre = 0
costo_entrada = 0
costo_plato_fuerte = 0
costo_guarnicion = 0
tiempo = 0
tiempo_final = 0


print("Porfavor selecciona tu entrada")
print("1. Ensalada")
print("2. Frigoles")
print("3. Mini tacos")
print("4. Pan")
entrada = int(input("Porfavor, selecciona tu opción, basandose en los números: "))

# Sumar el costo
def costoEntrada(entrada) :
    costo_entrada = costo_entrada + costo
    return costo_entrada

print("Porfavor selecciona tu plato fuerte")
print("1. Carne")
print("2. Pollo")
print("3. Chuleta")
print("4. Pescado")
plato_fuerte = int(input("Porfavor, selecciona tu opción, basandose en los números: "))

# Sumar el costo
def costoPlatoFuerte(plato_fuerte) :
    costo_plato_fuerte = costo_plato_fuerte + costo
    return costo_plato_fuerte

print("Porfavor selecciona tu guarnicion")
print("1. Tortillas")
print("2. Arroz")
print("3. Papas")
print("4. Ensalada")
guarnicion = int(input("Porfavor, selecciona tu opción, basandose en los números: "))

# Sumar el costo
def costoGuarnicion(guarnicion) :
    costo_guarnicion = costo_guarnicion + costo
    return costo_guarnicion

print("Porfavor selecciona tu postre")
print("1. Gelatina")
print("2. Pastel")
print("3. Alfajores")
print("4. Helado")
postre = int(input("Porfavor, selecciona tu opción, basandose en los números: "))

# Sumar el costo, además depende de lo que escogio se va sumando el tiempo
def costoPostre(postre) :
    costo_postre = costo_postre + costo
    return costo_postre


# Sumar la propina
print("Quiere agregar propina 1=Si, 2=No")

def Propina (propina):
    propina = input
    return propina

costoPostre(postre)
costo_final = costo_postre + costo_entrada + costo_guarnicion + costo_plato_fuerte + propina
print(costo_final)

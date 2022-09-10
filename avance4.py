# La variable "costo", es lo que va a tener cada entrada, plato fuerte, guarnicion, 
costo_final = 0
tiempo = 0
tiempo_final = 0

def costoEntrada(entrada,costo_entrada) :
    if entrada == 1:
        print("Porfavor escoja su tipo de ensalada")
        print("1. Cesar ($60)")
        print("2. Poke de atún ($65)")
        print("3. Panzanella ($70)")
        ensalada = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if ensalada == 1:
            costo_entrada = 60
        elif ensalada == 2:
            costo_entrada = 65
        elif ensalada == 3:
            costo_entrada = 70
    elif entrada == 2:
        print("Porfavor escoja su tipo de frijoles")
        print("1. Frijoles charros ($50)")
        print("2. Frijoles negros ($55)")
        print("3. Frijoles rojos ($60)")
        frijoles = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if frijoles == 1:
            costo_entrada = 50
        elif frijoles == 2:
            costo_entrada = 55
        elif frijoles == 3:
            costo_entrada = 60
    elif entrada == 3:
        print("Porfavor escoja su tipo de mini tacos")
        print("1. Mini tacos al pastor ($50)")
        print("2. Mini tacos de bistec ($50)")
        print("3. Mini tacos de carnitas ($50)")
        mini_tacos = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        costo_entrada = 50
    elif entrada == 4:
        palabra_entrada = "pan"
        print("Porfavor escoja su tipo de pan")
        print("1. Pan bolillo ($35)")
        print("2. Pan telera ($35)")
        print("3. Pan de avena ($40)")
        pan = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if pan == 1 or pan == 2:
            costo_entrada = 35
        elif pan == 3:
            costo_entrada = 40
    return costo_entrada

def costoPlatoFuerte(plato_fuerte,costo_plato_fuerte) :
    if plato_fuerte == 1:
        print("Porfavor escoja el tipo de carne")
        print("1. Milanesa ($90)")
        print("2. Asada ($85)")
        print("3. Guiso ($85)")
        carne = int(input("Porfavor selecciona tu opción, basandose en los números"))
        if carne == 1:
            costo_plato_fuerte = 90
        elif carne == 2 or carne == 3:
            costo_plato_fuerte = 85
    elif plato_fuerte == 2:
        print("Porfavor escoja el tipo de pollo")
        print("1. Milanesa ($90)")
        print("2. Sopa de pollo ($90)")
        print("3. Al horno ($90)")
        pollo = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if pollo == 1:
            costo_plato_fuerte = 90
        elif pollo == 2:
            costo_plato_fuerte = 85
        elif pollo == 3:
            costo_plato_fuerte = 85
    elif plato_fuerte == 3:
        print("Porfavor escoga el tipo de chuleta")
        print("1. Ahumada ($90)")
        print("2. Cocinada ($90)")
        print("3. A la plancha ($85)")
        chuleta = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if chuleta == 1:
            costo_plato_fuerte = 90
        elif chuleta == 2:
            costo_plato_fuerte = 90
        elif chuleta == 3:
            costo_plato_fuerte = 85
    elif plato_fuerte == 4:
        print("Porfavor escoge el tipo de pescado")
        print("1. Al vapor ($85)")
        print("2. Frito ($90)")
        print("3. Ceviche ($90)")
        pescado = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if pescado == 1:
            costo_plato_fuerte = 85
        elif pescado == 2 or pescado == 3:
            costo_plato_fuerte = 90
    return costo_plato_fuerte

# Sumar el costo
def costoGuarnicion(guarnicion,costo_guarnicion) :
    if guarnicion == 1:
        print("Porfavor escoja el tipo de tortilla")
        print("1. Maíz ($30)")
        print("2. Trigo ($30)")
        tortilla = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        costo_guarnicion = 30
    elif guarnicion == 2:
        print("Porfavor escoja el tipo de arroz")
        print("1. Blanco ($50)")
        print("2. Rojo ($55)")
        arroz = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if arroz == 1:
            costo_guarnicion = 50
        elif arroz == 2:
            costo_guarnicion = 55
    elif guarnicion == 3:
        print("Porfavor escoja el tipo de papas")
        print("1. Francesa ($65)")
        print("2. Fritas ($65)")
        print("3. Cocinadas ($60)")
        papas = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if papas == 1 or  papas == 2:
            costo_guarnicion = 65
        if papas == 3:
            costo_guarnicion = 60
    if guarnicion == 4:
        print("Porfavor escoja el tipo de ensalada: ")
        print("1. Cesar ($60)")
        print("2. Poke de atún ($65)")
        print("3. Panzanella ($70)")
        ensalada = int(input("Porfavor selecciona tu  opción, basandose en los números: "))
        if ensalada == 1:
            costo_guarnicion = 60
        if ensalada == 2:
            costo_guarnicion = 65
        if ensalada == 3:
            costo_guarnicion = 70
    return costo_guarnicion

# Sumar el costo, además depende de lo que escogio se va sumando el tiempo
def costoPostre(postre,costo_postre) :
    if postre == 1:
        print("Porfavor escoja el tipo de gelatina")
        print("1. Limón ($35)")
        print("2. Fresa ($35)")
        print("3. Durazno ($35)")
        gelatina = int(input("Porfavor selecciona tu opción, basandose el números: "))
        costo_postre = 35
    if postre == 2:
        print("Porfavor escoja el tipo de pastel")
        print("1. Tres leches ($45)")
        print("2. Chocolate ($40)")
        print("3. Mil hojas ($45)")
        pastel = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        if pastel == 1 or pastel == 3:
            costo_postre = 45
        if pastel == 2:
            costo_postre = 40
    if postre == 3:
        print("Porfavor escoja el tipo de alfajor")
        print("1. Chocolate ($40)")
        print("2. Vainilla ($40)")
        print("3. Marplatense (relleno y exterior de chocolate) ($40)")
        alfajor = int(input("Porfavor selecciona tu opción, basandose en los números: "))
        costo_postre = 40
    if postre == 4:
        print("Porfavor escoja el tipo de helado")
        print("1. Napolitano ($35)")
        print("2. Chocolate ($35)")
        print("3. Vainilla ($35)")
        helado = int(input("Porfavor selecciona tu opción, basandose en los números"))
        costo_postre = 35
    return costo_postre

def Propina(propina,costo_propina):
    costo_propina = 0
    costo_propina = int(input("Porfavor agrege la propina que quiera dar "))
    return costo_propina

opcion_entrada = int(input("¿Quiere agregar entrada? Si=1, No=2"))
costo_entrada = 0
if opcion_entrada == 1:
    print("Porfavor selecciona tu entrada")
    print("1. Ensalada")
    print("2. Frijoles")
    print("3. Mini tacos")
    print("4. Pan")
    entrada = int(input("Porfavor, selecciona tu opción, basandose en los números: "))
    while entrada < 0 or entrada > 5:
        print("Número incorrecto, porfavor digite basandose en las opciones")
        print("1. Ensalada")
        print("2. Frijoles")
        print("3. Mini tacos")
        print("4. Pan")
        entrada = int(input("Porfavor selecciona de nuevo tu opción: "))
    costo_entrada = costoEntrada(entrada,costo_entrada)

opcion_plato_fuerte = int(input("¿Quiere agregar plato fuerte? Si=1, No=2"))
costo_plato_fuerte = 0
if opcion_plato_fuerte == 1:
    print("Porfavor selecciona tu plato fuerte")
    print("1. Carne")
    print("2. Pollo")
    print("3. Chuleta")
    print("4. Pescado")
    plato_fuerte = int(input("Porfavor, selecciona tu opción, basandose en los números: "))
    while plato_fuerte < 0 or plato_fuerte > 5:
        print("Número incorrecto, porfavor digite basandose en las opciones")
        print("1. Carne")
        print("2. Pollo")
        print("3. Chuleta")
        print("4. Pescado")
        plato_fuerte = int(input("Porfavor selecciona de nuevo tu opción: "))
    costo_plato_fuerte = costoPlatoFuerte(plato_fuerte,costo_plato_fuerte)

opcion_guarnicion = int(input("¿Quiere agregar guarnición? Si=1, No=2"))
costo_guarnicion = 0
if opcion_guarnicion == 1:
    print("Porfavor selecciona tu guarnición")
    print("1. Tortillas")
    print("2. Arroz")
    print("3. Papas")
    print("4. Ensalada")
    guarnicion = int(input("Porfavor selecciona tu opción, basandose en los números: "))
    while entrada < 0 or entrada > 5:
        print("Número incorrecto, porfavor digite basandose en las opciones")
        print("1. Tortillas")
        print("2. Arroz")
        print("3. Papas")
        print("4. Ensalada")
        plato_fuerte = int(input("Porfavor selecciona de nuevo tu opción: "))
    costo_guarnicion = costoGuarnicion(guarnicion,costo_guarnicion)

opcion_postre = int(input("¿Quiere agregar postre? Si=1, No=2"))
costo_postre = 0
if opcion_postre == 1:
    print("Porfavor selecciona tu postre")
    print("1. Gelatina")
    print("2. Pastel")
    print("3. Alfajores")
    print("4. Helado")
    postre = int(input("Porfavor selecciona tu opció, basandose en los números: "))
    while postre < 0 or postre > 5:
        print("Número incorrecto, porfavor digite basandose en las opciones")
        print("1. Gelatina")
        print("2. Pastel")
        print("3. Alfajores")
        print("4. Helado")
    costo_postre = costoPostre(postre,costo_postre)

print("Quiere agregar propina 1=Si, 2=No")
propina = int(input("Porfavor agregar la propina"))
costo_propina = 0
if propina == 1:
    costo_propina = Propina(propina,costo_propina)

costo_final = costo_postre + costo_guarnicion + costo_entrada + costo_plato_fuerte + costo_propina
print(f"El costo final de su platillo es de {costo_final}")

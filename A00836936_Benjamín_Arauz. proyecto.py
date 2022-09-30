costo_final = 0
tiempo = 0
tiempo_final = 0

def costoEntrada(costo_entrada) :
    print("Porfavor selecciona tu entrada")
    lista_entrada = ["1. Ensalada","2. Frijoles","3. Mini tacos","4. Pan"]
    for entry in lista_entrada:
        print(entry)
    entrada = int(input("Porfavor, selecciona tu opción, basandose en los números\n"))
    while (entrada < 1) or (entrada > 4):
        print("Número no válido, porfavor digite basandose en las opciones")
        for not_entry in lista_entrada:
            print(not_entry)
        entrada = int(input("Porfavor selecciona de nuevo tu opción\n"))
    if entrada == 1:
        print("Porfavor escoja su tipo de ensalada")
        lista_ensalada = ["1. Cesar ($60)","2. Poke de atún ($65)","3. Panzanella ($70)"]
        for salad in lista_ensalada:
            print(salad)
        ensalada = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (ensalada < 1) or (ensalada > 3):
            print("Número no válido")
            for notsalad in lista_ensalada:
                print(notsalad)
            ensalada = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if ensalada == 1:
            costo_entrada = 60
        elif ensalada == 2:
            costo_entrada = 65
        elif ensalada == 3:
            costo_entrada = 70
    elif entrada == 2:
        print("Porfavor  escoja su tipo de frijoles")
        lista_frijoles = ["1. Frijoles charros ($50)","2. Frijoles negros ($55)","3. Frijoles rojos ($60)"]
        for beans in lista_frijoles:
            print(beans)
        frijoles = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (frijoles < 1) or (frijoles > 3):
            print("Número no válido")
            for notbeans in lista_frijoles:
                print(notbeans)
            frijoles = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if frijoles == 1:
            costo_entrada = 50
        elif frijoles == 2:
            costo_entrada = 55
        elif frijoles == 3:
            costo_entrada = 60
    elif entrada == 3:
        print("Porfavor escoja su tipo de mini tacos")
        lista_mini_tacos = ["1. Mini tacos al pastor ($50)","2. Mini tacos de bistec ($50)","3. Mini tacos de carnitas ($50)"]
        for small_tacos in lista_mini_tacos:
            print(small_tacos)
        mini_tacos = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (mini_tacos < 1) or (mini_tacos > 3):
            print("Número no válido")
            for not_small_tacos in lista_mini_tacos:
                print(not_small_tacos) 
            mini_tacos = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        costo_entrada = 50
    elif entrada == 4:
        print("Porfavor escoja su tipo de pan")
        lista_pan = ["1. Pan bolillo ($35)","2. Pan telera ($35)","3. Pan de avena ($40)"]
        for bread in lista_pan:
            print(bread)
        pan = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pan < 1) or (pan > 3):
            lista_pan1 = ["Número no válido",lista_pan]
            for not_bread in lista_pan:
                print(not_bread)
            pan = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if pan == 1 or pan == 2:
            costo_entrada = 35
        elif pan == 3:
            costo_entrada = 40
    return costo_entrada
def costoPlatoFuerte(costo_plato_fuerte):
    print("Porfavor selecciona tu plato fuerte")
    lista_plato_fuerte = ["1. Carne","2. Pollo","3. Chuleta","4. Pescado"]
    for main_course in lista_plato_fuerte:
        print(main_course)
    plato_fuerte = int(input("Porfavor, selecciona tu opción, basandose en los números\n"))
    while plato_fuerte < 0 or plato_fuerte > 5:
        print("Número no válido, porfavor digite basandose en las opciones")
        for not_main_course in lista_plato_fuerte:
            print(not_main_course)
        plato_fuerte = int(input("Porfavor selecciona de nuevo tu opción\n"))
    if plato_fuerte == 1:
        print("Porfavor escoja el tipo de carne")
        lista_carne = ["1. Milanesa ($90)","2. Asada ($85)","3. Guiso ($85)"]
        for meal in lista_carne:
            print(meal)
        carne = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (carne < 1) or (carne > 3):
            print("Número no válido")
            for not_meal in lista_carne:
                print(not_meal)
            carne = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if carne == 1:
            costo_plato_fuerte = 90
        elif carne == 2 or carne == 3:
            costo_plato_fuerte = 85
    elif plato_fuerte == 2:
        print("Porfavor escoja el tipo de pollo")
        lista_pollo = ["1. Milanesa ($90)","2. Sopa de pollo ($90)","3. Al horno ($90)"]
        for chicken in lista_pollo:
            print(chicken)
        pollo = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pollo < 1) or (pollo > 3):
            print("Número no válido")
            for not_chicken in lista_pollo:
                print(not_chicken)
            pollo = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        costo_plato_fuerte = 90
    elif plato_fuerte == 3:
        print("Porfavor escoga el tipo de chuleta")
        lista_chuleta = ["1. Ahumada ($90)","2. Cocinada ($90)","3. A la plancha ($85)"]
        for chop in lista_chuleta:
            print(chop)
        chuleta = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (chuleta < 1) or (chuleta > 3):
            print("Número no válido")
            for not_chop in lista_chuleta:
                print(not_chop)
            chuleta = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if chuleta == 1:
            costo_plato_fuerte = 90
        elif chuleta == 2:
            costo_plato_fuerte = 90
        elif chuleta == 3:
            costo_plato_fuerte = 85
    elif plato_fuerte == 4:
        print("Porfavor escoge el tipo de pescado")
        lista_pescado = ["1. Al vapor ($85)","2. Frito ($90)","3. Ceviche ($90)"]
        for fish in lista_pescado:
            print(fish)
        pescado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pescado < 1) or (pescado > 3):
            print("Número no válido")
            for not_fish in lista_pescado:
                print(not_fish)
            pescado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if pescado == 1:
            costo_plato_fuerte = 85
        elif pescado == 2 or pescado == 3:
            costo_plato_fuerte = 90
    return costo_plato_fuerte
def costoGuarnicion(costo_guarnicion):
    print("Porfavor selecciona tu guarnición")
    lista_guarnicion = ["1. Tortillas","2. Arroz","3. Papas","4. Ensalada"]
    for garrison in lista_guarnicion:
        print(garrison)
    guarnicion = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
    while guarnicion < 0 or guarnicion > 5:
        print("Número no válido, porfavor digite basandose en las opciones")
        for not_garrison in lista_guarnicion:
            print(not_garrison)
        guarnicion = int(input("Porfavor selecciona de nuevo tu opción\n"))
    if guarnicion == 1:
        print("Porfavor escoja el tipo de tortilla")
        lista_tortilla = ["1. Maíz ($30)","2. Trigo ($30)"]
        for tort in lista_tortilla:
            print(tort)
        tortilla = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (tortilla < 1) or (tortilla > 2):
            print("Número no válido")
            for not_tort in lista_tortilla:
                print(not_tort)
            tortilla = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        costo_guarnicion = 30
    elif guarnicion == 2:
        print("Porfavor escoja el tipo de arroz")
        lista_arroz = ["1. Blanco ($50)","2. Rojo ($55)"]
        for rice in lista_arroz:
            print(rice)
        arroz = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (arroz < 1) or (arroz > 2):
            print("Número no válido")
            for not_rice in lista_arroz:
                print(not_rice)
            arroz = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if arroz == 1:
            costo_guarnicion = 50
        elif arroz == 2:
            costo_guarnicion = 55
    elif guarnicion == 3:
        print("Porfavor escoja el tipo de papas")
        lista_papas = ["1. Francesa ($65)","2. Fritas ($65)","3. Cocinadas ($60)"]
        for potatoes in lista_papas:
            print(potatoes)
        papas = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (papas < 1) or (papas > 3):
            print("Número no válido")
            for not_potatoes in lista_papas:
                print(not_potatoes)
            papas = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if papas == 1 or  papas == 2:
            costo_guarnicion = 65
        if papas == 3:
            costo_guarnicion = 60
    if guarnicion == 4:
        print("Porfavor escoja el tipo de ensalada: ")
        lista_ensalada = ["1. Cesar ($60)","2. Poke de atún ($65)","3. Panzanella ($70)"]
        for salad in lista_ensalada:
            print(salad)
        ensalada = int(input("Porfavor selecciona tu  opción, basandose en los números\n"))
        while (ensalada < 1) or (ensalada > 3):
            print("Número no válido")
            for not_salad in lista_ensalada:
                print(not_salad)
            ensalada = int(input("Porfavor selecciona tu  opción, basandose en los números\n"))
        if ensalada == 1:
            costo_guarnicion = 60
        if ensalada == 2:
            costo_guarnicion = 65
        if ensalada == 3:
            costo_guarnicion = 70
    return costo_guarnicion
def costoPostre(costo_postre):
    print("Porfavor selecciona tu postre")
    lista_postre = ["1. Gelatina","2. Pastel","3. Alfajores","4. Helado"]
    for dessert in lista_postre:
        print(dessert)
    postre = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
    while postre < 0 or postre > 5:
        print("Número no válido, porfavor digite basandose en las opciones")
        for not_dessert in lista_postre:
            print(dessert)
        postre = int(input("Porfavor selecciona de nuevo tu opción\n"))
    if postre == 1:
        print("Porfavor escoja el tipo de gelatina")
        lista_gelatina = ["1. Limón ($35)","2. Fresa ($35)","3. Durazno ($35)"]
        for jelly in lista_gelatina:
            print(jelly)
        gelatina = int(input("Porfavor selecciona tu opción, basandose el números\n"))
        while (gelatina < 1) or (gelatina > 3):
            print("Número no válido")
            for not_jelly in lista_gelatina:
                print(not_jelly)
            gelatina = int(input("Porfavor selecciona tu opción, basandose el números\n"))
        costo_postre = 35
    if postre == 2:
        print("Porfavor escoja el tipo de pastel")
        lista_pastel = ["1. Tres leches ($45)","2. Chocolate ($40)","3. Mil hojas ($45)"]
        for cake in lista_pastel:
            print(cake)
        pastel = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pastel < 1) or (pastel > 3):
            print("Número no válido")
            for not_cake in lista_pastel:
                print(not_cake)
            pastel = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        if pastel == 1 or pastel == 3:
            costo_postre = 45
        if pastel == 2:
            costo_postre = 40
    if postre == 3:
        print("Porfavor escoja el tipo de alfajor")
        lista_alfajor = ["1. Chocolate ($40)","2. Vainilla ($40)","3. Marplatense (relleno y exterior de chocolate) ($40)"]
        for alf in lista_alfajor:
            print(alf)
        alfajor = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (alfajor < 1) or (alfajor > 3):
            print("Número no válido")
            for not_alf in lista_alfajor:
                print(not_alf)
            alfajor = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        costo_postre = 40
    if postre == 4:
        print("Porfavor escoja el tipo de helado")
        lista_helado = ["1. Napolitano ($35)","2. Chocolate ($35)","3. Vainilla ($35)"]
        for ice_cream in lista_helado:
            print(ice_cream)
        helado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (helado < 1) or (helado > 3):
            print("Número no válido")
            for not_ice_cream in lista_helado:
                print(not_ice_cream)
            helado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        costo_postre = 35
    return costo_postre
def Propina(costo_propina):
    costo_propina = int(input("Porfavor agregar la propina\n"))
    return costo_propina
opcion_entrada = int(input("¿Quiere agregar entrada? Si=1, No=2\n"))
costo_entrada = 0
while (opcion_entrada != 1) and (opcion_entrada != 2):
    opcion_entrada = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_entrada == 1:
    costo_entrada = costoEntrada(costo_entrada)
opcion_plato_fuerte = int(input("¿Quiere agregar plato fuerte? Si=1, No=2\n"))
costo_plato_fuerte = 0
while (opcion_plato_fuerte != 1) and (opcion_plato_fuerte != 2):
    opcion_plato_fuerte = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_plato_fuerte == 1:
    costo_plato_fuerte = costoPlatoFuerte(costo_plato_fuerte)
opcion_guarnicion = int(input("¿Quiere agregar guarnición? Si=1, No=2\n"))
costo_guarnicion = 0
while (opcion_guarnicion != 1) and (opcion_guarnicion!= 2):
    opcion_guarnicion = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_guarnicion == 1:
    costo_guarnicion = costoGuarnicion(costo_guarnicion)
opcion_postre = int(input("¿Quiere agregar postre? Si=1, No=2\n"))
costo_postre = 0
while (opcion_postre != 1) and (opcion_postre!= 2):
    opcion_postre = int(input("Número no válido, porfavor ingrese de nuevo (Si=1, No=2\n"))
if opcion_postre == 1:
    costo_postre = costoPostre(costo_postre)
opcion_propina = int(input("¿Quiere agregar propina? Si=1, 2=No\n"))
costo_propina = 0
while (opcion_propina != 1) and (opcion_propina != 2):
    opcion_propina = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_propina == 1:
    costo_propina = Propina(costo_propina)

costo_final = costo_postre + costo_guarnicion + costo_entrada + costo_plato_fuerte + costo_propina
print(f"El costo final de su platillo es de {costo_final}")
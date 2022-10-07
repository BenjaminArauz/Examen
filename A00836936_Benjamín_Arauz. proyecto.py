costo_final = 0
tiempo = 0
tiempo_final = 0
def costoEntrada(costo_entrada):
    palabra = '1. Entrada: '
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
        dic_ensalada = {
            "1. Cesar ($60)":15,
            "2. Poke de atún ($65)":20,
            "3. Panzanella ($70)":15
        }
        for salad in dic_ensalada:
            print(salad)
        ensalada = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (ensalada < 1) or (ensalada > 3):
            print("Número no válido")
            for notsalad in dic_ensalada:
                print(notsalad)
            ensalada = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        ensalada = str(ensalada)
        for price_salad in dic_ensalada:
            if price_salad[0] == ensalada:
                costo_entrada = int(price_salad[(price_salad.find("$")+1):(price_salad.find("$")+3)])
                tiempo_entrada = int(dic_ensalada[price_salad])
                if price_salad[0] == '2' or price_salad[0] == '3':
                    palabra += 'Ensalada de ' + price_salad[3:(price_salad.find("(")-1)].lower()
                else:
                    palabra += 'Ensalada ' + price_salad[3:(price_salad.find("(")-1)].lower()
    elif entrada == 2:
        print("Porfavor  escoja su tipo de frijoles")
        dic_frijoles = {
            "1. Frijoles charros ($50)":20,
            "2. Frijoles negros ($55)":15,
            "3. Frijoles rojos ($60)":20
        }
        for beans in dic_frijoles:
            print(beans)
        frijoles = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (frijoles < 1) or (frijoles > 3):
            print("Número no válido")
            for notbeans in dic_frijoles:
                print(notbeans)
            frijoles = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        frijoles = str(frijoles)
        for price_beans in dic_frijoles:
            if price_beans[0] == frijoles:
                costo_entrada = int(price_beans[(price_beans.find("$")+1):(price_beans.find("$")+3)])
                tiempo_entrada = int(dic_frijoles[price_beans])
                palabra += price_beans[3:(price_beans.find("(")-1)]
    elif entrada == 3:
        print("Porfavor escoja su tipo de mini tacos")
        dic_mini_tacos = {
            "1. Mini tacos al pastor ($50)":10,
            "2. Mini tacos de bistec ($50)":15,
            "3. Mini tacos de carnitas ($50)":15
        }
        for small_tacos in dic_mini_tacos:
            print(small_tacos)
        mini_tacos = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (mini_tacos < 1) or (mini_tacos > 3):
            print("Número no válido")
            for not_small_tacos in dic_mini_tacos:
                print(not_small_tacos) 
            mini_tacos = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        mini_tacos = str(mini_tacos)
        for price_tacos in dic_mini_tacos:
            if price_tacos[0] == mini_tacos:
                costo_entrada = int(price_tacos[(price_tacos.find("$")+1):(price_tacos.find("$")+3)])
                tiempo_entrada = int(dic_mini_tacos[price_tacos])
                palabra += price_tacos[3:(price_tacos.find("(")-1)]
    elif entrada == 4:
        print("Porfavor escoja su tipo de pan")
        dic_pan = {
            "1. Pan bolillo ($35)":5,
            "2. Pan telera ($35)":5,
            "3. Pan de avena ($40)":5
        }
        for bread in dic_pan:
            print(bread)
        pan = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pan < 1) or (pan > 3):
            print("Número no válido")
            for not_bread in dic_pan:
                print(not_bread)
            pan = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        pan = str(pan)
        for price_bread in dic_pan:
            if price_bread[0] == pan:
                costo_entrada = int(price_bread[(price_bread.find("$")+1):(price_bread.find("$")+3)])
                tiempo_entrada = int(dic_pan[price_bread])
                palabra += price_bread[3:(price_bread.find("(")-1)]
    return costo_entrada,tiempo_entrada,palabra
def costoPlatoFuerte(costo_plato_fuerte):
    palabra = '2. Plato fuerte: '
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
        dic_carne = {
            "1. Milanesa ($90)":30,
            "2. Asada ($85)":35,
            "3. Guiso ($85)":30
        }
        for meal in dic_carne:
            print(meal)
        carne = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (carne < 1) or (carne > 3):
            print("Número no válido")
            for not_meal in dic_carne:
                print(not_meal)
            carne = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        carne = str(carne)
        for price_meal in dic_carne:
            if price_meal[0] == carne:
                costo_plato_fuerte = int(price_meal[(price_meal.find("$")+1):(price_meal.find("$")+3)])
                tiempo_plato_fuerte = int(dic_carne[price_meal])
                if price_meal[0] == '1':
                    palabra += price_meal[3:(price_meal.find("(")-1)] +' de carne '
                elif price_meal[0] == '3':
                    palabra += 'Carne en '+ price_meal[3:(price_meal.find("(")-1)].lower()
                else:
                    palabra += 'Carne '+ price_meal[3:(price_meal.find("(")-1)].lower()
    elif plato_fuerte == 2:
        print("Porfavor escoja el tipo de pollo")
        dic_pollo = {
            "1. Milanesa ($90)":35,
            "2. Sopa de pollo ($90)":35,
            "3. Al horno ($90)":30
        }
        for chicken in dic_pollo:
            print(chicken)
        pollo = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pollo < 1) or (pollo > 3):
            print("Número no válido")
            for not_chicken in dic_pollo:
                print(not_chicken)
            pollo = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        pollo = str(pollo)
        for price_chicken in dic_pollo:
            if price_chicken[0] == pollo:
                costo_plato_fuerte = int(price_chicken[(price_chicken.find("$")+1):(price_chicken.find("$")+3)])
                tiempo_plato_fuerte = int(dic_pollo[price_chicken])
                if price_chicken[0] == '2':
                    palabra += price_chicken[3:(price_chicken.find("(")-1)]
                elif price_chicken[0] == '1':
                    palabra += price_chicken[3:(price_chicken.find("(")-1)] +' de pollo '
                else:
                    palabra += 'Pollo ' + price_chicken[3:(price_chicken.find("(")-1)].lower()
    elif plato_fuerte == 3:
        print("Porfavor escoga el tipo de chuleta")
        dic_chuleta = {
            "1. Ahumada ($90)":45,
            "2. Cocinada ($90)":45,
            "3. A la plancha ($85)":40
        }
        for chop in dic_chuleta:
            print(chop)
        chuleta = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (chuleta < 1) or (chuleta > 3):
            print("Número no válido")
            for not_chop in dic_chuleta:
                print(not_chop)
            chuleta = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        chuleta = str(chuleta)
        for price_chop in dic_chuleta:
            if price_chop[0] == chuleta:
                costo_plato_fuerte = int(price_chop[(price_chop.find("$")+1):(price_chop.find("$")+3)])
                tiempo_plato_fuerte = int(dic_chuleta[price_chop])
                palabra += 'Chuleta ' + price_chop[3:(price_chop.find("(")-1)].lower()
    elif plato_fuerte == 4:
        print("Porfavor escoge el tipo de pescado")
        dic_pescado = {
            "1. Al vapor ($85)":35,
            "2. Frito ($90)":40,
            "3. Ceviche ($90)":35
        }
        for fish in dic_pescado:
            print(fish)
        pescado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pescado < 1) or (pescado > 3):
            print("Número no válido")
            for not_fish in dic_pescado:
                print(not_fish)
            pescado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        pescado = str(pescado)
        for price_fish in dic_pescado:
            if price_fish[0] == pescado:
                costo_plato_fuerte = int(price_fish[(price_fish.find("$")+1):(price_fish.find("$")+3)])
                tiempo_plato_fuerte = int(dic_pescado[price_fish])
                if price_fish[0] == '3':
                    palabra += price_fish[3:(price_fish.find("(")-1)] + ' de pescado'
                else:
                    palabra += 'Pescado ' + price_fish[3:(price_fish.find("(")-1)].lower()
    return costo_plato_fuerte,tiempo_plato_fuerte,palabra
def costoGuarnicion(costo_guarnicion):
    palabra = '3. Guarnición: '
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
        dic_tortilla = {
            "1. Maíz ($30)":5,
            "2. Trigo ($30)":5
        }
        for tort in dic_tortilla:
            print(tort)
        tortilla = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (tortilla < 1) or (tortilla > 2):
            print("Número no válido")
            for not_tort in dic_tortilla:
                print(not_tort)
            tortilla = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        tortilla = str(tortilla)
        for price_tortilla in dic_tortilla:
            if price_tortilla[0] == tortilla:
                costo_guarnicion = int(price_tortilla[(price_tortilla.find("$")+1):(price_tortilla.find("$")+3)])
                tiempo_guarnicion = int(dic_tortilla[price_tortilla])
                palabra += 'Tortilla de ' + price_tortilla[3:(price_tortilla.find("(")-1)].lower()
    elif guarnicion == 2:
        print("Porfavor escoja el tipo de arroz")
        dic_arroz = {
            "1. Blanco ($50)":25,
            "2. Rojo ($55)":30
        }
        for rice in dic_arroz:
            print(rice)
        arroz = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (arroz < 1) or (arroz > 2):
            print("Número no válido")
            for not_rice in dic_arroz:
                print(not_rice)
            arroz = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        arroz = str(arroz)
        for price_rice in dic_arroz:
            if price_rice[0] == arroz:
                costo_guarnicion = int(price_rice[(price_rice.find("$")+1):(price_rice.find("$")+3)])
                tiempo_guarnicion = int(dic_arroz[price_rice])
                palabra += 'Arroz ' + price_rice[3:(price_rice.find("(")-1)].lower()
    elif guarnicion == 3:
        print("Porfavor escoja el tipo de papas")
        dic_papas = {
            "1. Francesa ($65)":30,
            "2. Fritas ($65)":25,
            "3. Cocinadas ($60)":25
        }
        for potatoes in dic_papas:
            print(potatoes)
        papas = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (papas < 1) or (papas > 3):
            print("Número no válido")
            for not_potatoes in dic_papas:
                print(not_potatoes)
            papas = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        papas = str(papas)
        for price_potatoes in dic_papas:
            if price_potatoes[0] == papas:
                costo_guarnicion = int(price_potatoes[(price_potatoes.find("$")+1):(price_potatoes.find("$")+3)])
                tiempo_guarnicion = int(dic_papas[price_potatoes])
                if price_potatoes[0] == '1':
                    palabra += 'Papas a la ' + price_potatoes[3:(price_potatoes.find("(")-1)].lower()
                else:
                    palabra += 'Papas ' + price_potatoes[3:(price_potatoes.find("(")-1)].lower()
    elif guarnicion == 4:
        print("Porfavor escoja el tipo de ensalada: ")
        dic_ensalada = {
            "1. Cesar ($60)":15,
            "2. Poke de atún ($65)":20,
            "3. Panzanella ($70)":15
        }
        for salad in dic_ensalada:
            print(salad)
        ensalada = int(input("Porfavor selecciona tu  opción, basandose en los números\n"))
        while (ensalada < 1) or (ensalada > 3):
            print("Número no válido")
            for not_salad in dic_ensalada:
                print(not_salad)
            ensalada = int(input("Porfavor selecciona tu  opción, basandose en los números\n"))
        ensalada = str(ensalada)
        for price_salad in dic_ensalada:
            if price_salad[0] == ensalada:
                costo_guarnicion = int(price_salad[(price_salad.find("$")+1):(price_salad.find("$")+3)])
                tiempo_guarnicion = int(dic_ensalada[price_salad])
                if price_salad[0] == '2' or price_salad[0] == '3':
                    palabra += 'Ensalada de ' + price_salad[3:(price_salad.find("(")-1)].lower()
                else:
                    palabra += 'Ensalada ' + price_salad[3:(price_salad.find("(")-1)].lower()
    return costo_guarnicion,tiempo_guarnicion,palabra
def costoPostre(costo_postre):
    palabra = '4. Postre: '
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
        dic_gelatina = {
            "1. Limón ($35)":5,
            "2. Fresa ($35)":5,
            "3. Durazno ($35)":5
        }
        for jelly in dic_gelatina:
            print(jelly)
        gelatina = int(input("Porfavor selecciona tu opción, basandose el números\n"))
        while (gelatina < 1) or (gelatina > 3):
            print("Número no válido")
            for not_jelly in dic_gelatina:
                print(not_jelly)
            gelatina = int(input("Porfavor selecciona tu opción, basandose el números\n"))
        gelatina = str(gelatina)
        for price_jelly in dic_gelatina:
            if price_jelly[0] == gelatina:
                costo_postre = int(price_jelly[(price_jelly.find("$")+1):(price_jelly.find("$")+3)])
                tiempo_postre = int(dic_gelatina[price_jelly])
                palabra += 'Helado de ' + price_jelly[3:(price_jelly.find("(")-1)].lower()
    if postre == 2:
        print("Porfavor escoja el tipo de pastel")
        dic_pastel = {
            "1. Tres leches ($45)":35,
            "2. Chocolate ($40)":30,
            "3. Mil hojas ($45)":35
        }
        for cake in dic_pastel:
            print(cake)
        pastel = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (pastel < 1) or (pastel > 3):
            print("Número no válido")
            for not_cake in dic_pastel:
                print(not_cake)
            pastel = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        pastel = str(pastel)
        for price_cake in dic_pastel:
            if price_cake[0] == pastel:
                costo_postre = int(price_cake[(price_cake.find("$")+1):(price_cake.find("$")+3)])
                tiempo_postre = int(dic_pastel[price_cake])
                palabra += 'Pastel de ' + price_cake[3:(price_cake.find("(")-1)].lower()
    if postre == 3:
        print("Porfavor escoja el tipo de alfajor")
        dic_alfajor = {
            "1. Chocolate ($40)":15,
            "2. Vainilla ($40)":10,
            "3. Marplatense (relleno y exterior de chocolate) ($40)":15
        }
        for alf in dic_alfajor:
            print(alf)
        alfajor = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (alfajor < 1) or (alfajor > 3):
            print("Número no válido")
            for not_alf in dic_alfajor:
                print(not_alf)
            alfajor = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        alfajor = str(alfajor)
        for price_alf in dic_alfajor:
            if price_alf[0] == alfajor:
                costo_postre = int(price_alf[(price_alf.find("$")+1):(price_alf.find("$")+3)])
                tiempo_postre = int(dic_alfajor[price_alf])
                palabra += 'Alfajor de ' + price_alf[3:(price_alf.find("(")-1)].lower()
    if postre == 4:
        print("Porfavor escoja el tipo de helado")
        dic_helado = {
            "1. Napolitano ($35)":10,
            "2. Chocolate ($35)":10,
            "3. Vainilla ($35)":10
        }
        for ice_cream in dic_helado:
            print(ice_cream)
        helado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        while (helado < 1) or (helado > 3):
            print("Número no válido")
            for not_ice_cream in dic_helado:
                print(not_ice_cream)
            helado = int(input("Porfavor selecciona tu opción, basandose en los números\n"))
        helado = str(helado)
        for price_ice_cream in dic_helado:
            if price_ice_cream[0] == helado:
                costo_postre = int(price_ice_cream[(price_ice_cream.find("$")+1):(price_ice_cream.find("$")+3)])
                tiempo_postre = int(dic_helado[price_ice_cream])
                if price_ice_cream[0] == '1':
                    palabra += 'Helado ' + price_ice_cream[3:(price_ice_cream.find("(")-1)].lower()
                else:
                    palabra += 'Helado de ' + price_ice_cream[3:(price_ice_cream.find("(")-1)].lower()
    return costo_postre,tiempo_postre,palabra
def Propina(costo_propina):
    costo_propina = int(input("Porfavor agregar la propina\n"))
    return costo_propina
lista_palabras = []    
opcion_entrada = int(input("¿Quiere agregar entrada? Si=1, No=2\n"))
costo_entrada = 0
tiempo_entrada = 0
palabra_entrada = ''
while (opcion_entrada != 1) and (opcion_entrada != 2):
    opcion_entrada = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_entrada == 1:
    costo_entrada,tiempo_entrada,palabra_entrada = costoEntrada(costo_entrada)
    lista_palabras.append(palabra_entrada)
opcion_plato_fuerte = int(input("¿Quiere agregar plato fuerte? Si=1, No=2\n"))
costo_plato_fuerte = 0
tiempo_plato_fuerte = 0
palabra_plato_fuerte = ''
while (opcion_plato_fuerte != 1) and (opcion_plato_fuerte != 2):
    opcion_plato_fuerte = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_plato_fuerte == 1:
    costo_plato_fuerte,tiempo_plato_fuerte,palabra_plato_fuerte = costoPlatoFuerte(costo_plato_fuerte)
    lista_palabras.append(palabra_plato_fuerte)
opcion_guarnicion = int(input("¿Quiere agregar guarnición? Si=1, No=2\n"))
costo_guarnicion = 0
tiempo_guarnicion = 0
palabra_guarnicion = ''
while (opcion_guarnicion != 1) and (opcion_guarnicion!= 2):
    opcion_guarnicion = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_guarnicion == 1:
    costo_guarnicion,tiempo_guarnicion,palabra_guarnicion = costoGuarnicion(costo_guarnicion)
    lista_palabras.append(palabra_guarnicion)
opcion_postre = int(input("¿Quiere agregar postre? Si=1, No=2\n"))
costo_postre = 0
tiempo_postre = 0
palabra_postre = ''
while (opcion_postre != 1) and (opcion_postre!= 2):
    opcion_postre = int(input("Número no válido, porfavor ingrese de nuevo (Si=1, No=2\n"))
if opcion_postre == 1:
    costo_postre,tiempo_postre,palabra_postre = costoPostre(costo_postre)
    lista_palabras.append(palabra_postre)
opcion_propina = int(input("¿Quiere agregar propina? Si=1, 2=No\n"))
costo_propina = 0
while (opcion_propina != 1) and (opcion_propina != 2):
    opcion_propina = int(input("Número no válido, porfavor ingrese de nuevo Si=1, No=2\n"))
if opcion_propina == 1:
    costo_propina = Propina(costo_propina)
print("El resumen de su platillo es:")
for word in lista_palabras:
    print(word)
costo_final = costo_postre + costo_guarnicion + costo_entrada + costo_plato_fuerte + costo_propina
print(f"El costo final de su platillo es de {costo_final}")
tiempo_final = max(tiempo_entrada,tiempo_plato_fuerte,tiempo_guarnicion,tiempo_postre)
print(f"El tiempo estimado que se va a demorar su platillo es {tiempo_final}-{tiempo_final+5} minutos")
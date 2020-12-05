import MapReduce
import sys
import getopt
import re
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pprint


mr = MapReduce.MapReduce()

continentes = ['europa', 'sudamerica']

sudamerica = [
    'Argentina',
    'Bolivia',
    'Brazil',
    'Chile',
    'Colombia',
    'Ecuador',
    'Guyana',
    'Paraguay',
    'Peru',
    'Suriname',
    'Venezuela',
    'Uruguay']

europa = [
    'Albania',
    'Andorra',
    'Armenia',
    'Austria',
    'Azerbaijan',
    'Belarus',
    'Belgium',
    'Bosnia and Herzegovina',
    'Bulgaria',
    'Croatia',
    'Cyprus',
    'Czechia',
    'Denmark',
    'Estonia',
    'Finland',
    'France',
    'Georgia',
    'Germany',
    'Greece',
    'Hungary',
    'Iceland',
    'Ireland',
    'Israel',
    'Italy',
    'Kazakhstan',
    'Kyrgyzstan',
    'Latvia',
    'Lithuania',
    'Luxembourg',
    'Malta',
    'Monaco',
    'Montenegro',
    'Netherlands',
    'North Macedonia',
    'Norway',
    'Poland',
    'Portugal',
    'Republic of Moldova',
    'Romania',
    'Russian Federation',
    'San Marino',
    'Serbia',
    'Slovakia',
    'Slovenia',
    'Spain',
    'Sweden',
    'Switzerland',
    'Tajikistan',
    'Turkey',
    'Turkmenistan',
    'Ukraine',
    'United Kingdom',
    'Uzbekistan',
]

total = {}
edad_total = {}

validador = 'mundo'

continente = 'all'

pais = 'all'

genero = 'all'

generos = ['male','female']

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    # key = (record[2], record[4], record[1])
    key = (record[2], record[1], record[4])
    value = record[5]
    # words = value.split()

    # ---- TU CODIGO AQUI ----
    # para cada palabra w en la lista 'words' emite  (w,1)
    # usa mr.emit_intermediate
    # ------------------------
    # print('clave: ' + key)
    # print('valor:' + value)
    if validador == 'europa' and record[1] in europa:
        if genero != 'all' and record[3] == genero:
            mr.emit_intermediate(key, value)
        elif genero == 'all':
            mr.emit_intermediate(key, value)
    elif validador == 'sudamerica' and record[1] in sudamerica:
        if genero != 'all' and record[3] == genero:
            mr.emit_intermediate(key, value)
        elif genero == 'all':
            mr.emit_intermediate(key, value)
    elif validador == 'mundo':
        if genero != 'all' and record[3] == genero:
            mr.emit_intermediate(key, value)
        elif genero == 'all':
            mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # ---- TU CODIGO AQUI ----
    # emite (key, longitud list_of_values)
    # usa mr.emit
    # ------------------------
    sum = 0
    for value in list_of_values:
        sum += int(value)
    validate_total(key, sum)
    mr.emit((key, sum))


def validate_total(key, sum):
    if key[0] in total.keys():
        total[key[0]] += sum
    else:
        total[key[0]] = sum

    if key[2] in edad_total.keys():
        if key[0] in edad_total[key[2]].keys():
            edad_total[key[2]][key[0]] += sum
        else:
            edad_total[key[2]][key[0]] = sum
    else:
        edad_total[key[2]] = {}
        edad_total[key[2]][key[0]] = sum


def manage_options(argv):
    global validador
    global pais
    global genero

    try:
      opts, args = getopt.getopt(argv, "hc:p:g:", ["continente=", "pais=","genero="])
    except getopt.GetoptError:
      print('Uso: Grafica.py [-c <continente>] [-p <pais>] [-g <genero>] [-h]')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Grafica.py [-c <continente>] [-p <pais>] [-g <genero>] [-h]')
            sys.exit()
        elif opt in ("-c", "--continente"):
            if arg in continentes:
                validador = arg
            else:
                print('Parametro enviado no es valido, utilizando valor mundo para trabajar con todos los datos')
        elif opt in ("-p", "--pais"):
            pais = arg
            print('Opcion p activado, se ignorará opcion c')
        elif opt in ("-g", "--genero"):
            if arg in generos:
                genero = arg
            else:
                print('Parametro enviado no es valido, utilizando valor all para trabajar con todos los datos')


# Do not modify below this line
# =============================
if __name__ == '__main__':
    manage_options(sys.argv[1:])
    
    # mr.execute(inputdata, mapper, reducer)
    lista = []
    client = MongoClient(
        "mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.ProyectoBD
    # serverStatusResult = db.command("serverStatus")}

    if pais != 'all':
        validador = 'mundo'
        resultado = db.Suicidios.find({'year': {'$gt': '1999', '$lt':'2016'}, 'country': pais})
    else:
        resultado = db.Suicidios.find({'year': {'$gt': '1999', '$lt':'2016'}})

    if resultado is None:
        print("La consulta a la base no arrojo resultados, terminando programa")
        sys.exit()

    for object in resultado:
        # print(object.values())
        listaSTR = "["
        contador = True
        for elemento in list(object.values()):
            if contador:
                listaSTR += "\""
                contador = False
            else:
                listaSTR += ",\""
            listaSTR += str(elemento) + "\""
        listaSTR += "]\n"
        lista.append(listaSTR)

    mr.execute(lista, mapper, reducer)

    filename = message = validador

    if pais != 'all':
        filename = pais
        message = 'pais ' + pais
    
    if genero != 'all':
        filename += '_' + genero
        message += ' buscando por genero \'' + genero + '\'' 

    plt.figure(figsize=(20,10))
    x = []
    y = []
    for key in sorted(total.keys()):
        x.append(key)
        y.append(total[key])
    plt.plot(x,y)
    plt.savefig(filename+'.png')

    print('Generado grafica de numeros de suicidios en el '+ message  +' desde el año 2000 al 2015')
    print('Grafica guardada en ' + filename + '.png')

    plt.figure(figsize=(20,10))
    for edad in edad_total:
        x = []
        y = []
        for key in sorted(edad_total[edad].keys()):
            x.append(key)
            y.append(edad_total[edad][key])
        plt.plot(x,y)
    plt.savefig('RangoEdad_'+ filename+'.png')

    print('Generado grafica de numeros de suicidios por rango de edad en el '+ message +' desde el año 2000 al 2015')
    print('Grafica guardada en RangoEdad_'+ filename+'.png')

    

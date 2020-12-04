import MapReduce
import sys
import re
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pprint


mr = MapReduce.MapReduce()

latinoamerica = [
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

latino = {}
edad_latino = {}

europe = {}
edad_europe = {}

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    #key = (record[2], record[4], record[1])
    key = (record[2], record[1],record[4])
    value = record[5]
    #words = value.split()

    # ---- TU CODIGO AQUI ----
    # para cada palabra w en la lista 'words' emite  (w,1)
    # usa mr.emit_intermediate
    # ------------------------
    #print('clave: ' + key)
    #print('valor:' + value)
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
    validate_sudamerica(key,sum)
    validate_europa(key,sum)
    mr.emit((key, sum))


def validate_sudamerica(key, sum):
    if key[1] in latinoamerica:
        if key[0] in latino.keys():
            latino[key[0]] += sum
        else:
            latino[key[0]] = sum
        if key[2] in edad_latino.keys():
            if key[0] in edad_latino[key[2]].keys():
                edad_latino[key[2]][key[0]] += sum
            else:
                edad_latino[key[2]][key[0]] = sum
        else:
            edad_latino[key[2]] = {}
            edad_latino[key[2]][key[0]] = sum

def validate_europa(key, sum):
    if key[1] in europa:
        if key[0] in europe.keys():
            europe[key[0]] += sum
        else:
            europe[key[0]] = sum
        if key[2] in edad_europe.keys():
            if key[0] in edad_europe[key[2]].keys():
                edad_europe[key[2]][key[0]] += sum
            else:
                edad_europe[key[2]][key[0]] = sum
        else:
            edad_europe[key[2]] = {}
            edad_europe[key[2]][key[0]] = sum


# Do not modify below this line
# =============================
if __name__ == '__main__':
    #inputdata = open(sys.argv[1])
    #mr.execute(inputdata, mapper, reducer)
    lista = []
    client = MongoClient(
        "mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.ProyectoBD
    # serverStatusResult = db.command("serverStatus")}

    resultado = db.Suicidios.find({'year': {'$gt': '1999', '$lt':'2016'}})
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

    plt.figure(figsize=(20,10))
    plt.plot(latino.keys(),latino.values())
    plt.savefig('latino.png')

    print('Generado grafica de numeros de suicidios en Sudamérica desde el año 2000 al 2015')
    print('Grafica guardada en latino.png')

    plt.figure(figsize=(20,10))
    for edad in edad_latino:
        plt.plot(edad_latino[edad].keys(),edad_latino[edad].values())
    plt.savefig('RangoEdad_latino.png')

    print('Generado grafica de numeros de suicidios por rango de edad en Sudamérica desde el año 2000 al 2015')
    print('Grafica guardada en RangoEdad_latino.png')
    
    plt.figure(figsize=(20,10))
    plt.plot(europe.keys(),europe.values())
    plt.savefig('europe.png')

    print('Generado grafica de numeros de suicidios en Europa desde el año 2000 al 2015')
    print('Grafica guardada en europe.png')

    plt.figure(figsize=(20,10))
    for edad in edad_europe:
        plt.plot(edad_europe[edad].keys(),edad_europe[edad].values())
    plt.savefig('RangoEdad_europa.png')

    print('Generado grafica de numeros de suicidios por rango de edad en Europa desde el año 2000 al 2015')
    print('Grafica guardada en RangoEdad_europa.png')

    

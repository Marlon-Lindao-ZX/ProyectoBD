import MapReduce
import sys
import getopt
import re
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pprint
import numpy as np


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

    query = {}

    if pais != 'all':
        validador = 'mundo'
        query = {'year': {'$gt': '1999', '$lt':'2016'}, 'country': pais}
        resultado = db.Suicidios.find({'year': {'$gt': '1999', '$lt':'2016'}, 'country': pais})
    else:
        if validador == 'mundo':
            query = {'year': {'$gt': '1999', '$lt':'2016'}}
        elif validador == 'europa':
            query = {'year': {'$gt': '1999', '$lt':'2016'}, 'country': {'$in':europa}}
        else:
            query = {'year': {'$gt': '1999', '$lt':'2016'}, 'country': {'$in':sudamerica}}

    if genero == 'male':
        query['sex'] = 'male'
    elif genero == 'female':
        query['sex'] = 'female'

    resultado = db.Suicidios.find(query)

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

    title1 = 'Grafica de distribuicion de numeros de suicidios por año en '
    title2 = 'Grafica de distribucion de numeros de suicidios por año separados por rango de edad en '

    filename = message = validador

    if pais != 'all':
        filename = pais
        message = 'pais ' + pais
        title1 += pais
        title2 += pais
    else:
        title1 += validador
        title2 += validador

    title1 += '\n'
    title2 += '\n'
    
    if genero != 'all':
        filename += '_' + genero
        message += ' buscando por genero \'' + genero + '\''
        title1 +=  ' buscando por genero \'' + genero + '\''
        title2 +=  ' buscando por genero \'' + genero + '\''

    plt.figure()
    fig, ax = plt.subplots(figsize=(20,10))
    ax.set_title(title1)
    ax.set_ylabel('Numero de Suicidios') 
    ax.set_xlabel('Año') 
    x = []
    y = []
    for key in sorted(total.keys()):
        x.append(key)
        y.append(total[key])
    ax.plot(x,y)
    ax.grid(axis="y")
    ax.grid(axis="x")

    yticks = ax.get_yticks()
    xticks = ax.get_xticks()

    for ytick in yticks[1:-2]:
        for xtick in xticks:
            ax.vlines(xtick, ytick-0.05, ytick, linewidth=0.5)
    plt.savefig(filename+'.png')
    plt.close()

    print('Generado grafica de numeros de suicidios en el '+ message  +' desde el año 2000 al 2015')
    print('Grafica guardada en ' + filename + '.png')

    plt.figure(figsize=(20,10))
    fig, ax = plt.subplots(figsize=(20,10))
    ax.set_title(title2)
    ax.set_ylabel('Numero de Suicidios') 
    ax.set_xlabel('Año') 
    for edad in sorted(edad_total):
        x = []
        y = []
        for key in sorted(edad_total[edad].keys()):
            x.append(key)
            y.append(edad_total[edad][key])
        ax.plot(x,y,label='Rango: ' + str(edad))
    #ax.stackplot(listadoX[0], listadoY, labels=rangos)
    
    #ax.set_yticks(np.arange(minimo, maximo, (maximo - minimo) / 10))
    
    ax.grid(axis="y")
    ax.grid(axis="x")

    yticks = ax.get_yticks()
    xticks = ax.get_xticks()

    for ytick in yticks[1:-2]:
        for xtick in xticks:
            ax.vlines(xtick, ytick-0.05, ytick, linewidth=0.5)

    plt.legend(loc="upper right")
    plt.savefig('RangoEdad_'+ filename+'.png')
    plt.close()

    print('Generado grafica de numeros de suicidios por rango de edad en el '+ message +' desde el año 2000 al 2015')
    print('Grafica guardada en RangoEdad_'+ filename+'.png')

    

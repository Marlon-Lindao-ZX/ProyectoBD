import MapReduce
from time import time
import sys
import re
from pymongo import MongoClient
import pprint


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    id = record[0]
    country = record[1]
    year = record[2]
    genre = record[3]
    range_age = record[4]
    n_suicidios = record[5]
    coord1 = record[6]
    x = record[7]
    y = record[8]
    z = record[9]
    a = record[10]
    b = record[11]
    generation = record[12]

    mr.emit_intermediate(generation,n_suicidios)


def reducer(key, list_of_values):
    #Acumulador
    sum=0
    for i in list_of_values:
        sum += int(i)
    mr.emit((key,sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    lista = []
    client = MongoClient("mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.ProyectoBD
    #serverStatusResult = db.command("serverStatus")}
    '''
    a = db.Suicidios.count_documents({'sex':'male','year':'2016'})
    b    = db.Suicidios.count_documents({'sex':'female','year':'2016'})
    c = db.Suicidios.count_documents({'year':'2016'})
    print(a)
    print(b)
    print(c)
    '''
    resultado = db.Suicidios.find({'year':{'$gt':'1999'}})
    
    for object in resultado:
        #print(object.values())
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
    timeAntes = time()
    
    mr.execute(lista, mapper, reducer)
    timeFinal = time() - timeAntes
    print("Tiempo de consulta de registros en la base: %0.05f segundos." % timeFinal)
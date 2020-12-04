import MapReduce
import sys
import re
from pymongo import MongoClient
import pprint
import csv


# Do not modify below this line
# =============================
if __name__ == '__main__':
    #inputdata = open(sys.argv[1])
    #mr.execute(inputdata, mapper, reducer)
    lista = []
    client = MongoClient("mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.ProyectoBD
    #serverStatusResult = db.command("serverStatus")}
    db.Suicidios2.drop()
    keys = []
    objetos = []
    with open('master.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                i = 0
                for r in row:
                    if i == 0:
                        keys.append('country')
                    else:
                        keys.append(r)
                    i += 1
                line_count += 1
            else:
                i = 0
                d = {}
                for r in row:
                    d[keys[i]] = r
                    i += 1
                objetos.append(d)
                line_count += 1
    print(f'Processed {line_count} lines.')

    db.Suicidios2.insert_many(objetos)
    
    resultado = db.Suicidios2.count_documents({})

    print(f'Cantidad de Objetos en la Coleccion: {resultado} objetos.')
  
    
  

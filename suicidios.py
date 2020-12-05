import MapReduce
import sys
import re
from pymongo import MongoClient
import pprint


mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = (record[2],record[4])
    value = record[5]
    #words = value.split()

    # ---- TU CODIGO AQUI ----
    # para cada palabra w en la lista 'words' emite  (w,1)
    # usa mr.emit_intermediate
    # ------------------------
    #print('clave: ' + key)
    #print('valor:' + value)
    mr.emit_intermediate(key,value)

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
    mr.emit((key,sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  #inputdata = open(sys.argv[1])
  #mr.execute(inputdata, mapper, reducer)
  lista = []
  client = MongoClient("mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
  db = client.ProyectoBD
  #serverStatusResult = db.command("serverStatus")}
  '''
  a = db.Suicidios.count_documents({'sex':'male','year':'2016'})
  b = db.Suicidios.count_documents({'sex':'female','year':'2016'})
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
      
  #print(lista)
   
  mr.execute(lista, mapper, reducer)
  '''
  resultado = db.Suicidios.find({'country':'Ecuador'})
  for object in resultado:
    pprint.pprint(object)
    '''
    
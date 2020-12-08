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
    client = MongoClient(
        "mongodb+srv://sDsVuNPCSUTtObcH:sDsVuNPCSUTtObcH@cluster0.rjqka.mongodb.net/test?authSource=admin&replicaSet=atlas-zmesu9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.ProyectoBD
    # serverStatusResult = db.command("serverStatus")}
    db.Suicidios.drop()
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

    db.Suicidios.insert_many(objetos)

    resultado = db.Suicidios.count_documents({})

    print(f'Cantidad de Objetos en la Coleccion: {resultado} objetos.')

    print('Consulta #1')

    resultado = db.Suicidios.count_documents(
        {'year': {'$gt': '1999'}, 'year': {'$lt': '2005'}})
    print(f'Numero de datos encontrados: {resultado} objetos.')

    resultado = db.Suicidios.find(
        {'year': {'$gt': '1999'}, 'year': {'$lt': '2005'}},)
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Consulta #2')

    resultado = db.Suicidios.count_documents(
        {'generation': 'Generation X', 'country': 'Ecuador'})
    print(f'Numero de datos encontrados: {resultado} objetos.')

    resultado = db.Suicidios.find(
        {'generation': 'Generation X', 'country': 'Ecuador'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Insert #1')
    post1 = {
        'country': "Venezuela",
        'year': "1987",
        'sex': "male",
        'age': "15-24 years",
        'suicides_no': "210",
        'population': "312900",
        'suicides/100k pop': "6.71",
        'country-year': "Venezuela1987",
        'HDI for year': "",
        'gdp_for_year($)': "2,156,624,900",
        'gdp_per_capita($)': "796",
        'generation': "Generation X"
    }

    db.Suicidios.insert_one(post1)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Insert #2')

    post2 = {
        'country': "Venezuela",
        'year': "1987",
        'sex': "female",
        'age': "15-24 years",
        'suicides_no': "210",
        'population': "312900",
        'suicides/100k pop': "6.71",
        'country-year': "Venezuela1987",
        'HDI for year': "",
        'gdp_for_year($)': "2,156,624,900",
        'gdp_per_capita($)': "796",
        'generation': "Generation Z"
    }

    db.Suicidios.insert_one(post2)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Update #1')

    query = {'country': 'Venezuela'}

    newValue = {"$set": { "year": "2001" }}

    db.Suicidios.update_one(query,newValue)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Update #2')

    query = {'country': 'Venezuela'}

    newValue = {"$set": { "generation": "Silent" }}

    db.Suicidios.update_many(query,newValue)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Delete #1')

    query = {'country':'Venezuela','year':'2001'}

    db.Suicidios.delete_one(query)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1

    print('Delete #2')

    query = {'country':'Venezuela'}

    db.Suicidios.delete_many(query)

    resultado = db.Suicidios.find(
        {'country': 'Venezuela'})
    i = 1
    for object in resultado:
        print('#' + str(i) + ':')
        pprint.pprint(object)
        i += 1
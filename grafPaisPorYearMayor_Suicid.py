import numpy as np
import matplotlib.pyplot as plt
import random

l=[]

f=open("kk.txt","r")
l=[]
for i in f.readlines():
    i_ne=i.split("\n")
    k=i_ne[0].split("'")
    n_l=[]
    t=(k[1],k[3])
    #n_l.append(t)
    g=k[4].split(" ")
    t_n=(t,g[1][:-1])
    l.append(t_n)
    
    #l.append(i[0])
diccionario={}


for valor_lista in l:
    if valor_lista[0][1] in diccionario.keys():
        elemento_interno = diccionario[valor_lista[0][1]]
        n_suicidio=list(elemento_interno.values())[0]
        if int(valor_lista[1]) > int(n_suicidio):
            pais_anterior=list(elemento_interno.keys())[0]
            elemento_interno.pop(pais_anterior)
            pais_nuevo=valor_lista[0][0]
            elemento_interno[pais_nuevo]=valor_lista[1]  
    else:
        diccionario[valor_lista[0][1]]={valor_lista[0][0]:valor_lista[1]}
print(diccionario)
    

years=[]
pais=[]
numero_suicidio=[]

for key, value in diccionario.items():
    years.append(key)
    
    pais.append(str(list(value.keys())[0]))
    numero_suicidio.append(int(list(value.values())[0]))


def millions(x, pos):
    """The two args are the value and tick position."""
    return '{:2.0f}'.format(x)


def generar_color():
    colores=[]
    for i in range(len(years)):
        color = "%06x" % random.randint(0, 0xFFFFFF)
        color = "#"+color
        colores.append(color)


    return colores
colores=generar_color()
fig, ax = plt.subplots()

for x, y in zip(years, numero_suicidio):
    plt.text(x , y,'%.0f' % y, ha='center', va='bottom',color="red")
for i,c in zip(pais,colores):
    ax.plot(19, 30, color=c, label=i)

fig.set_size_inches(300, 250)
ax.legend(loc="upper right", title="Paises", frameon=False)
ax.yaxis.set_major_formatter(millions)
ax.bar(years, numero_suicidio,color=colores,label="x")


#plt.show()
plt.savefig("numSuicidPorPais.png")
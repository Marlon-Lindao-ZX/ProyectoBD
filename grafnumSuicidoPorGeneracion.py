import random
import numpy as np

import matplotlib.pyplot as plt



f=open("kk.txt","r")
tuplas=[]
for i in f.readlines():
    print(i)
    i_ne=i.split("\n")
    k=i_ne[0].split(",")
    total=k[1][1:-1:]
    
    k=k[0][2:-1:]
    
    n_l=[]
    t=(k,str(total))
    tuplas.append(t)


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
elementos =[]
for i in range(len(tuplas)):
  elementos.append(str(tuplas[i][1])+" "+str(tuplas[i][0]))



data = [float(x.split()[0]) for x in elementos]
ingredients = [x.split()[-1] for x in elementos]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def generar_color():
    colores=[]
    for i in range(len(tuplas)):
        color = "%06x" % random.randint(0, 0xFFFFFF)
        color = "#"+color
        print(color)
        colores.append(color)


    return colores
colores=generar_color()

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Generaciones",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=7, weight="bold")

ax.set_title("Porcentaje de suicidios entre el año 2000 y 2016")

#plt.show()
plt.savefig("numSuicidPorGeneration.png")
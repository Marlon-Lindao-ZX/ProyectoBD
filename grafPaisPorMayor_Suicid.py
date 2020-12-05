from suicidios import mr
import numpy as np

import matplotlib.pyplot as plt

tuplas=tuple([["Generation X", 954111],
["Silent", 997466],
["G.I. Generation", 21633],
["Boomers", 1214360],
["Millenials", 606893],
["Generation Z", 15906]])

print(tuplas)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["954111 GenerationX",
            "997466 Silent",
            "21633 G.I.Generation",
          "1214360 Boomers",
          "606893 Millenials",
          "15906 GenerationZ"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

#plt.show()
plt.savefig("numSuicidPorGeneration.png")
from suicidios import mr

import numpy as np
import matplotlib.pyplot as plt

aay=([["2000", "G.I. Generation"], 21633],
[["2003", "Millenials"], 32431],
[["2003", "Boomers"], 98693],
[["2002", "Millenials"], 33151],
[["2005", "Silent"], 79037],
[["2004", "Millenials"], 30541],
[["2005", "Millenials"], 29398],
[["2006", "Silent"], 79416],
[["2007", "Generation X"], 37936],
[["2007", "Generation Z"], 1671],
[["2009", "Generation Z"], 1835],
[["2007", "Boomers"], 85749],
[["2009", "Boomers"], 90390],
[["2009", "Silent"], 83386],
[["2010", "Generation X"], 125681],
[["2000", "Generation X"], 73347],
[["2000", "Boomers"], 97814],
[["2005", "Boomers"], 88498],
[["2006", "Millenials"], 29692],
[["2008", "Silent"], 81242],
[["2006", "Boomers"], 87032],
[["2007", "Silent"], 80382],
[["2008", "Millenials"], 28145],
[["2000", "Millenials"], 2065],
[["2001", "Silent"], 80474],
[["2002", "Generation X"], 41536],
[["2002", "Silent"], 82733],
[["2004", "Generation X"], 38221],
[["2007", "Millenials"], 27670],
[["2008", "Generation Z"], 1640],
[["2000", "Silent"], 60973],
[["2001", "Generation X"], 40279],
[["2001", "Boomers"], 96998],
[["2003", "Silent"], 83902],
[["2003", "Generation X"], 41053],
[["2001", "Millenials"], 32901],
[["2004", "Silent"], 79568],
[["2010", "Millenials"], 27684],
[["2010", "Silent"], 83577],
[["2006", "Generation X"], 37221],
[["2008", "Generation X"], 37756],
[["2008", "Boomers"], 86664],
[["2009", "Generation X"], 39389],
[["2009", "Millenials"], 28487],
[["2010", "Generation Z"], 1760],
[["2002", "Boomers"], 98675],
[["2005", "Generation X"], 37442],
[["2004", "Boomers"], 92531],
[["2012", "Millenials"], 62905],
[["2013", "Silent"], 24153],
[["2012", "Silent"], 24578],
[["2014", "Silent"], 24865],
[["2015", "Millenials"], 53959],
[["2014", "Boomers"], 57696],
[["2015", "Generation Z"], 1681],
[["2013", "Generation X"], 80227],
[["2014", "Generation X"], 79132],
[["2015", "Generation X"], 71298],
[["2012", "Generation X"], 82482],
[["2013", "Boomers"], 57696],
[["2012", "Generation Z"], 1752],
[["2013", "Millenials"], 59317],
[["2014", "Generation Z"], 1882],
[["2013", "Generation Z"], 1806],
[["2015", "Silent"], 23114],
[["2015", "Boomers"], 53588],
[["2014", "Millenials"], 59409],
[["2012", "Boomers"], 58443],
[["2011", "Boomers"], 59178],
[["2011", "Millenials"], 65873],
[["2011", "Generation X"], 85345],
[["2011", "Silent"], 24209],
[["2011", "Generation Z"], 1879],
[["2016", "Silent"], 1857],
[["2016", "Millenials"], 3265],
[["2016", "Boomers"], 4715],
[["2016", "Generation X"], 5766])

generaciones=["Generation X","Silent", "G.I. Generation", "Boomers", "Millenials","Generation Z"]
tupl_generacion=[0,0,0,0,0,0]
years =[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
#lista=[tupl_generacion,tupl_generacion,tupl_generacion,tupl_generacion,tupl_generacion,tupl_generacion

# listaG=[]
# for union in range(len(years)):
#     l=[]
#     l.append(str(years[union]))
#     l.append(tupl_generacion)
#     #l.append(str((years[union])) + ", "+ str(tupl_generacion))
#     listaG.append(l)
# print(listaG)
#0 x
#1 silent
#2 gi 
#3 boomer
#4 millenial
#5 z
# a=([["2000", "G.I. Generation"], 21633],
# [["2003", "Millenials"], 32431],
# [["2003", "Boomers"], 98693],
# [["2002", "Millenials"], 33151],
# [["2005", "Silent"], 79037],
# [["2004", "Millenials"], 30541],
# [["2005", "Millenials"], 29398],
# [["2006", "Silent"], 79416],
# [["2007", "Generation X"], 37936],
# [["2007", "Generation Z"], 1671],
# [["2009", "Generation Z"], 1835],
# [["2007", "Boomers"], 85749],
# [["2009", "Silent"], 83386],
# [["2010", "Generation X"], 125681],
# [["2000", "Boomers"], 97814],
# [["2005", "Boomers"], 88498],
# [["2006", "Millenials"], 29692])
# print(len(a))
# for i in range(len(a)):
#     print(a[i])
#     print(a[i][0][0])
#     print(a[i][1])
#     if(a[i][0][0]=="2000"):
#         print("entra al año: "+str(a[i][0][0]))
#         for  generation in range(len(generaciones)):
        
        
#             if(a[i][0][1]==generaciones[generation]):
    
#                 print("2do if"+str(a[i][0][1]) +" "+ str(generaciones[generation]))
        
                
#                 for y in range(len(years)):
#                     print("valor de y "+str(years[y]))
#                     if(a[i][0][0]==listaG[y][0]):
#                         print("entra")
#                         print(a[i][0][0])
#                         print(listaG[y][0])
#                         print(str(a[i][0][0]) + str(a[i][1]) + "debe ser igual " + str(listaG[y][1][generation]))
#                         print(listaG[y])
#                         print(listaG[y][1])
#                         print(listaG[y][0])
#                         print(listaG[y][1][generation])
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
                
            
#     elif (a[i][0][0]=="2001"):
#         print("entra al año: "+str(a[i][0][0]))
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)                
                
            
#     elif (a[i][0][0]=="2002"):
#         print("entra al año: "+str(a[i][0][0]))
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2003"):
#         print("entra al año: "+str(a[i][0][0]))
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2004"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2005"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2006"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2007"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2008"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2009"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2010"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2011"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2012"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2013"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
                
#     elif (a[i][0][0]=="2014"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)        
                
#     elif (a[i][0][0]=="2015"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)        
                
#     elif (a[i][0][0]=="2016"):
#         for  generation in range(len(generaciones)):
    
    
#             if(a[i][0][1]==generaciones[generation]):
    
        
        
#                 for y in range(len(years)):
#                     if(a[i][0][0]==listaG[y][0]):
#                         listaG[y][1][generation]=a[i][1]
#         print(listaG)
#     else:
#         print("no entro")
             
    
# print(listaG)
# print(a)

##     print(a[i][0][0]a[i][0][1] + str(i[1]))
        

# for i in aay:
##     print(a[i][0][0]a[i][0][1] + str(i[1])) año, generacion y total


diccionario ={}
for i in aay:
    #print(i)
    #print(str(diccionario.keys()) + " " + str(diccionario.values()))
    if i[0][0] in diccionario.keys():
        n_clave = diccionario[i[0][0]]
        #print(i[0][1])
        if i[0][1] in n_clave.keys():
            n_clave[i[0][1]]=i[1]
            #print(str(n_clave[i[0][1]]) + " "+ str(i[1]))
    else:
        diccionario[i[0][0]]={"Generation X":0,"Silent":0, "G.I. Generation":0, "Boomers":0, "Millenials":0,"Generation Z":0}
        n_clave = diccionario[i[0][0]]
        #print(i[0][1])
        if i[0][1] in n_clave.keys():
            n_clave[i[0][1]]=i[1]
            #print(str(n_clave[i[0][1]]) + " "+ str(i[1]))
#print(diccionario)

lista_year=[]
l_n_suicid=[]
for clave in sorted(diccionario):
    
    lista_year.append(clave)
    n_lista=[]
    for n_clave in sorted(diccionario[clave]):
        n_lista.append(diccionario[clave][n_clave])
        # data = ((0, 1,2), (1, 3,4), (2, 3,4), (5, 8,9), (5, 1,300))
    #convert_tupla= tuple()
    l_n_suicid.append(tuple(n_lista))
lista_year=tuple(lista_year)
l_n_suicid=tuple(l_n_suicid)
#print(lista)
print(lista_year)
print(l_n_suicid)
#"Generation X","Silent", "G.I. Generation", "Boomers", "Millenials","Generation Z"
dim = len(lista_year)
print(dim)
w = 2.75
dimw = w / dim

fig, ax = plt.subplots()
x = np.arange(len(l_n_suicid))
print(x)
for i in range(len(l_n_suicid[0])):
   
    y = [d[i] for d in l_n_suicid]
  
    b = ax.bar(x + i * dimw, y, dimw, bottom=0)
   

ax.set_xticks(x + dimw / 2)
ax.set_xticklabels(map(str, lista_year))
ax.set_yscale('log')
ax.set_xlabel('x')
ax.set_ylabel('y')
#plt.show()
plt.savefig("figura.png")
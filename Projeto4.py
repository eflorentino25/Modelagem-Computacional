###Projeto 4


#import time
import networkx as nx
#import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
#from random import *
#from decimal import *
import os

#Declaração de variáveis.
Test = 0 




G = nx.Graph()



#Adicionando os nós ao Grafo a partir do arquivo do professor.
os.chdir('D:\\UNIFESP\\ModComp\\RedeModularizada')

arestas_txt = open('network.dat','r')

for line in arestas_txt:
    linhacomp = line.split()
    primeiro = linhacomp[0]
    segundo  = linhacomp[1]
    G.add_edge(primeiro, segundo)
#    print(primeiro,"HAHA",segundo)     
#    Test +=1
#    if(Test >= 5):
#        break
#Apresentar gráfico
#nx.draw(G, with_labels = True)    
#plt.draw()
#plt.show()    

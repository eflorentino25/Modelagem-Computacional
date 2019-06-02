# Projeto 4
#import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from random import *
#from decimal import *
import os
import sys

#%matplotlib inline
%matplotlib notebook


#np.set_printoptions(5000)
np.set_printoptions(threshold=sys.maxsize)#ver matriz sem truncamento

#--------------------------------------
#Declaração de variáveis.
#--------------------------------------
Test = 0 
n=1000 # número de nós 
grau=4 # grau médio de ligação 

#--------------------------------------

# Escolha da rede
#--------------------------------------
print('Qual topologia deseja utilizar?\n')
print(" 'B' - Barabasi \n 'N' - regular\n 'T' - From txt \n 'E' - Erdös-Rényi \n")
R = input('Topologia: ')

if R == "B" or R == "b": #BARABASI
    G = nx.barabasi_albert_graph(n,grau)
    
elif R == "N" or R == "n": #REGULAR
    G = nx.Graph(n,grau) 
    
elif R == "T" or R == "t": #Por arquivo de Texto
    G = nx.Graph()     
#Adicionando os nós ao Grafo a partir do arquivo do professor.
    os.chdir('C:\\Users\\Ellen')
    #os.chdir('//storage//emulated//0')
    #path = input('Digite o caminho completo (duas "//") até o arquivo ex: C://Eduardo//MODCOMP//grafos.dat')
    #path = input('Digite o caminho completo (duas "//") até o arquivo ex: C://Users//Ellen//network.dat')
    #os.chdir(path)
    
    arestas_txt = open('network.dat','r')
   
    for line in arestas_txt:
        
        linhacomp = line.split()
        primeiro = linhacomp[0]
        segundo  = linhacomp[1]
        G.add_edge(primeiro, segundo)
      
elif R == "E" or R == "e":   #Erdös-Rényi;
    nx.fast_gnp_random_graph(n,0.08,seed = 9)
 

#TESTES
#    print(primeiro,"HAHA",segundo)     
#    Test +=1
#    if(Test >= 5):
#        break
#Apresentar gráfico
# pos = nx.spring_layout(G)
# plt.figure(0,figsize=(35,35))
# nx.draw(G,pos,node_size=200,node_color ='yellow',edge_color='orange', with_labels = False) 
# nx.draw_networkx_labels(G,pos, font_size=25, font_color='k', font_family='sans-serif', font_weight='normal')
# plt.draw()
# plt.show() 
#FIMDETESTES 



#--------------------------------------
# Criação da matriz de adjacencia randomica (peso das arestas) e array randomico (peso dos nós)
#--------------------------------------

L= nx.to_numpy_matrix(G)# gera matriz de adjacencia das arestas: 1= nós ligados, 0=nós desligados

for i in range (0,n,1): # Dá valores randomicos (de 0 a 1) para a matriz L ao invés de apenas '1´s'
    for j in range (0,n,1):
        L[i,j]=random()*L[i,j]
#print(L)


S=[]# 
for i in range (0,n,1): # gera valores randomicos (de 0 a 1) para os nós. 1= máximo de resistência, 0= infectado
    value=random()
    S.append(value)
    
#--------------------------------------
# Selecionando alguns nós para serem contaminados e plot da rede inicial
#--------------------------------------   
S[0]=0 # nó 0 infectado inicialmente
S[1]=0 # nó 1 infectado inicialmente
S[2]=0 # nó 2 infectado inicialmente
S[7]=0 # nó 7 infectado inicialmente
S[6]=0 # nó 6 infectado inicialmente
S[4]=0 # nó 4 infectado inicialmente
S[601]=0 # nó 601 infectado inicialmente
S[496]=0 # nó 496 infectado inicialmente
S[38]=0 # nó 38 infectado inicialmente


pos = nx.spring_layout(G)
color_map0 = []
i=0
for node in G:
        if S[i]==0:
            color_map0.append('red')
        else: color_map0.append('green')
        i=i+1
plt.figure(0,figsize=(10,10))
nx.draw(G,pos,fixed=pos,node_size=50,node_color = color_map0,with_labels = False)
plt.show()#plotando rede inicial

#--------------------------------------
# cálculo de infecção, início das iterações
#--------------------------------------

for k in range (0,5,1):# calculo de contaminação, 5 iterações
    for i in range (0,n,1):
        for j in range (0,n,1):
            if S[j]==0 and L[i,j]>0 and (random()*10*S[i]/L[i,j]<0.5):
                    S[i]=0 
    color_map = []
    i=0
    for node in G:
        if S[i]==0:
            color_map.append('red')
        else: color_map.append('green')
        i=i+1
    plt.figure(k+1,figsize=(10,10))
    nx.draw(G,pos,fixed=pos,node_size=50,node_color = color_map,with_labels = False)
    plt.show()#plotando rede em cada iteração
    
print("Número de infectados: ",S.count(0))# conta número de infectados: S[i]=0


#--------------------------------------
# Informação do grafo e dos nós para auxiliar na análise
#--------------------------------------
#list(G.neighbors('1'))# mostra vizinhos do nó 'n'
#print(nx.info(G, '987'))# mostra informações do nó 'n'
#print(nx.info(G))# mostra informações do grafo G
#print(nx.degree_histogram(G)) # histograma de G
#degrees = [(node,val) for (node, val) in G.degree()] # mostra lista de nós por grau, do maior para o menor  
# print(sorted(G.degree, key=lambda x: x[1], reverse=True)) # (contnuação) mostra lista de nós por grau, do maior para o menor  
#A= sorted(G.degree, key=lambda x: x[1], reverse=True); # salva lista de nós por grau em um vetor
#print('(Número do nó de maior grau, Grau do nó):',A[0]) 
#maxdegree = A[0][0] # salva numero do nó de maior grau


#--------------------------------------
#Inicio da criação dos gráfos:
#--------------------------------------
#Plot do grafo
# plt.figure(1,figsize=(24,24)) 
# nx.draw(G,node_size=60)
# plt.show()

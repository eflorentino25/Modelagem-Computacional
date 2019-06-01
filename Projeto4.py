##Projeto 4
#import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
from random import *
#from decimal import *
import os
import sys

np.set_printoptions(threshold=sys.maxsize)#ver matriz sem truncamento

#--------------------------------------
#Declaração de variáveis.
#--------------------------------------
Test = 0 
G = nx.Graph()
n=1000 # número de nós 
g=4 # grau médio de ligação 

#--------------------------------------
# Escolha da rede
#--------------------------------------
R = input("Deseja gerar o grafo a partir de um arquivo? (S/N)")

if( R == 'S' or R == 's'): 
#Adicionando os nós ao Grafo a partir do arquivo do professor.
   #os.chdir('//storage//emulated//0')
   os.chdir('C:\\Users\\Ellen')

   arestas_txt = open('network.dat','r')
   
   for line in arestas_txt:
       linhacomp = line.split()
       primeiro = linhacomp[0]
       segundo  = linhacomp[1]
       G.add_edge(primeiro, segundo)
    
else:
    G = nx.barabasi_albert_graph(n,g)

#TESTES
#    print(primeiro,"HAHA",segundo)     
#    Test +=1
#    if(Test >= 5):
#        break
#Apresentar gráfico
#nx.draw(G, with_labels = True)    
#plt.draw()
#plt.show() 
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
S[0]=0 # nó 0 infectado inicialmente
S[1]=0 # nó 1 infectado inicialmente
S[2]=0 # nó 2 infectado inicialmente
# S[7]=0 # nó 7 infectado inicialmente
# S[6]=0 # nó 6 infectado inicialmente
# S[4]=0 # nó 4 infectado inicialmente
#print('S inicial:',S)

#--------------------------------------
# cálculo de infecção, início das iterações
#--------------------------------------

for k in range (0,5,1):# calculo de contaminação, 5 iterações
    for i in range (0,n,1):
        for j in range (0,n,1):
            if S[j]==0 and L[i,j]>0 and (random()*10*S[i]/L[i,j]<0.5):
                    S[i]=0
#print('S final: ',S)
print("Número de infectados: ",S.count(0))# conta número de infectados: S[i]=0


#--------------------------------------
# Informação do grafo e dos nós
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

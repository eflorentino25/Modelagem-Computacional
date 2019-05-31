###Projeto 4
#import time
import networkx as nx
#import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#import pandas as pd
#from random import *
#from decimal import *
import os

#Declaração de variáveis.
Test = 0 

G = nx.Graph()

R = input("Deseja gerar o grafo a partir de um arquivo? (S/N)")


if( R == 'S' or R == 's'): 
#Adicionando os nós ao Grafo a partir do arquivo do professor.
   os.chdir('C:\\Users\\Ellen')
   
   arestas_txt = open('network.dat','r')
   
   for line in arestas_txt:
       linhacomp = line.split()
       primeiro = linhacomp[0]
       segundo  = linhacomp[1]
       G.add_edge(primeiro, segundo)
    
else:
    G = nx.barabasi_albert_graph(1000, 2)



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
# Informação do grafo e dos nós
#--------------------------------------
#list(G.neighbors('1'))# mostra vizinhos do nó 'n'
#print(nx.info(G, '987'))# mostra informações do nó 'n'
#print(nx.info(G))# mostra informações do grafo G
print(nx.degree_histogram(G)) # histograma de G
degrees = [(node,val) for (node, val) in G.degree()] # mostra lista de nós por grau, do maior para o menor  
# print(sorted(G.degree, key=lambda x: x[1], reverse=True)) # (contnuação) mostra lista de nós por grau, do maior para o menor  
A= sorted(G.degree, key=lambda x: x[1], reverse=True); # salva lista de nós por grau em um vetor
print('(Número do nó de maior grau, Grau do nó):',A[0]) 
maxdegree = A[0][0] # salva numero do nó de maior grau 

#--------------------------------------
#Inicio da criação dos gráfos:
#--------------------------------------
# #Plot do grafo
# plt.figure(1,figsize=(24,24)) 
# nx.draw(G,node_size=60)
# plt.show() 

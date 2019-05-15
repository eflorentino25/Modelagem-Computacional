##Projeto 3
##############################################################################
##
##############################################################################


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import *

np.set_printoptions(threshold=sys.maxsize) #visualise matrix without truncation
#numpy.set_printoptions(threshold=2) #visualise matrix with truncation

n=6# number of nodes

x=[]# empty matrix of x
y=[]# empty matrix of y
for i in range (0,n+1,1): # generate random initial values for x and y 
    value=random()
    x.append(value)
    #print(x)
    value=random()
    y.append(value)
    #print(y)
    


A= np.matrix([[0,1,1,0,0,0],[1,0,0,1,0,0],[1,0,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,1],[0,0,0,0,1,0]])# test adjacency matrix


#ba = nx.barabasi_albert_graph(500, 2)#generate barabasi_albert matrix with 500 nodes and 2 edges
#A = nx.to_numpy_matrix(ba)# generate adjacency matrix 
#print(A)


S=np.zeros(n) # array for values of coupling
Si=[] # stores values of S
dt=1 #time increment

w=0.1 # coupling force
theta=0.5 # cutting threshold
I=0.2 # external stimulus
p=0 # noise signal
e=0.02 # model parameter epsilon
a=6 # model parameter alpha
b=0.1 # model parameter beta

for t in range (0,1,1):# iteration begin (0,end time Tmáx,increment=1)
    for i in range (0,n,1):# calculation of coupling influence, changing i index of A[i][j] 
        S[i]=0
        for j in range (0,6,1):# calculation of coupling influence, changing j index of A[i][j] 
            if A[i,j]==1 and x[j]>theta:
                S[i]=S[i]+w
        Si.append(S[i]) # attach S[i] to Si
    
    dx=np.zeros(n)
    dy=np.zeros(n)
    for k in range (0,n,1):# integration of neurons with Euler method
            dx[k]=(3*x[k]-(x[k]*x[k])-y[k]+I+p+S[k])*dt
            dy[k]=(e*(a*(1+np.tanh(x[k]/b))-y[k]))*dt
            x[k+1]=x[k]+dx[k]
            y[k+1]=y[k]+dy[k]
            print("x: ",x[k])
            print("y: ",y[k])



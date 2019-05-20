##Projeto 3
##############################################################################
##
##############################################################################


################ REDE REGULAR - 100% ACTIVE 100% COUPLING #################### or
################ REDE ERDÕS-RÉNYI - 100% ACTIVE 100% COUPLING #################### or
################ REDE BARABÁSI-ALBERT - 100% ACTIVE 100% COUPLING ####################

import time
start = time.time() # Start processing time

%matplotlib inline

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import *

n=500 # number of nodes

Tmax=1500# number of iterations, multiple of ten
dt=0.18 #time increment

k0=0 # sample number 0
k1=n*.1 # sample number 1
k2=n*.2 # sample number 2
k3=n*.3 # sample number 3
k4=n*.4 # sample number 4
k5=n*.5 # sample number 5
k6=n*.6 # sample number 6
k7=n*.7 # sample number 7
k8=n*.8 # sample number 8
k9=n*.9# sample number 9

ba = nx.cycle_graph(n) # or
#ba = nx.erdos_renyi_graph(n,0.00788) # degree 2 or
#ba = nx.erdos_renyi_graph(n,0.018) # degree 4 or
#ba = nx.barabasi_albert_graph(n,2)
A = nx.to_numpy_matrix(ba)# generate adjacency matrix 

w=0.1 # coupling force
theta=0.5 # cutting threshold
#I1 e I2: external stimulus
p=0 # noise signal
e=0.2 # model parameter epsilon
a=6 # model parameter alpha
b=0.1 # model parameter beta

x=[]# empty matrix of x
y=[]# empty matrix of y
for i in range (0,n,1): # generate random initial values for x and y 
    value=(4*random()-2)
    x.append(value)
    #print(x)
    value=4*random()
    y.append(value)
    #print(y)

S=np.zeros(n) # array for values of coupling

X0=[] # stores x values of node 0, separeted plots
X1=[]
X2=[]
X3=[]
X4=[]
X5=[] 
X6=[]
X7=[]
X8=[]
X9=[] # stores x values of node 9, separeted plots

x0=[] # stores x values of node 0, overlapping plots
x1=[]
x2=[]
x3=[]
x4=[]
x5=[] 
x6=[]
x7=[]
x8=[]
x9=[] # stores x values of node 9, overlapping plots

T=[] # stores t values
   
for t in range (0,Tmax,1):# iteration begin (0,end time Tmáx,increment=1)
    T.append(t)
    for i in range (0,n,1):# calculation of coupling influence, changing i index of A[i][j] 
        S[i]=0
        for j in range (0,n,1):# calculation of coupling influence, changing j index of A[i][j] 
            if A[i,j]==1 and x[j]>theta:
                S[i]=S[i]+w
    
    dx=np.zeros(n)
    dy=np.zeros(n)
    
    for k in range (0,int(n/2),1):# integration of neurons with Euler method
        I1=0.2 # active= 0.2 ; inactive=-0.02
        dx[k]=(3*x[k]-(x[k]*x[k]*x[k])+2-y[k]+I1+p+S[k])*dt # with coupling
        #dx[k]=(3*x[k]-(x[k]*x[k]*x[k])+2-y[k]+I1+p)*dt # without coupling
        dy[k]=(e*(a*(1+np.tanh(x[k]/b))-y[k]))*dt
        x[k]=x[k]+dx[k]
        y[k]=y[k]+dy[k]
        if k==k0:
            X0.append(x[k]+5)
            x0.append(x[k])
        if k==k1:
            X1.append(x[k]+10)
            x1.append(x[k])
        if k==k2:
            X2.append(x[k]+15)
            x2.append(x[k])
        if k==k3:
            X3.append(x[k]+20)
            x3.append(x[k])
        if k==k4:
            X4.append(x[k]+25)
            x4.append(x[k])
        if k==k5:
            X5.append(x[k]+30)
            x5.append(x[k])
        if k==k6:
            X6.append(x[k]+35)
            x6.append(x[k])
        if k==k7:
            X7.append(x[k]+40)
            x7.append(x[k])
        if k==k8:
            X8.append(x[k]+45)
            x8.append(x[k])
        if k==k9:
            X9.append(x[k]+50)
            x9.append(x[k])
            
    for k in range (int(n/2),n,1):# integration of neurons with Euler method
        I2=0.2 # active= 0.2 ; inactive=-0.02
        dx[k]=(3*x[k]-(x[k]*x[k]*x[k])+2-y[k]+I2+p+S[k])*dt # with coupling
        #dx[k]=(3*x[k]-(x[k]*x[k]*x[k])+2-y[k]+I2+p)*dt # without coupling
        dy[k]=(e*(a*(1+np.tanh(x[k]/b))-y[k]))*dt
        x[k]=x[k]+dx[k]
        y[k]=y[k]+dy[k]
        if k==k0:
            X0.append(x[k]+5)
            x0.append(x[k])
        if k==k1:
            X1.append(x[k]+10)
            x1.append(x[k])
        if k==k2:
            X2.append(x[k]+15)
            x2.append(x[k])
        if k==k3:
            X3.append(x[k]+20)
            x3.append(x[k])
        if k==k4:
            X4.append(x[k]+25)
            x4.append(x[k])
        if k==k5:
            X5.append(x[k]+30)
            x5.append(x[k])
        if k==k6:
            X6.append(x[k]+35)
            x6.append(x[k])
        if k==k7:
            X7.append(x[k]+40)
            x7.append(x[k])
        if k==k8:
            X8.append(x[k]+45)
            x8.append(x[k])
        if k==k9:
            X9.append(x[k]+50)
            x9.append(x[k])



######### Plot of nodes #########

plt.figure(1,figsize=(24,12))

########### separeted plot
plt.plot( T, X0, 'k')# time vs x , node 0
plt.plot( T, X1, 'r')# time vs x , node 1
plt.plot( T, X2, 'b')# time vs x , node 2
plt.plot( T, X3, 'c')# time vs x , node 3
plt.plot( T, X4, 'y')# time vs x , node 4
plt.plot( T, X5, 'g')# time vs x , node 5
plt.plot( T, X6, 'tab:orange')# time vs x , node 6
plt.plot( T, X7, 'tab:brown')# time vs x , node 7
plt.plot( T, X8, 'aquamarine')# time vs x , node 8
plt.plot( T, X9, 'lime')# time vs x , node 9

########### overlapping plot
plt.plot( T, x0, 'k')# time vs x , node 0
plt.plot( T, x1, 'r')# time vs x , node 1
plt.plot( T, x2, 'b')# time vs x , node 2
plt.plot( T, x3, 'c')# time vs x , node 3
plt.plot( T, x4, 'y')# time vs x , node 4
plt.plot( T, x5, 'g')# time vs x , node 5
plt.plot( T, x6, 'tab:orange')# time vs x , node 6
plt.plot( T, x7, 'tab:brown')# time vs x , node 7
plt.plot( T, x8, 'aquamarine')# time vs x , node 8
plt.plot( T, x9, 'lime')# time vs x , node 9

plt.grid(True)
plt.axis([-100, Tmax, -5, 55])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


########### Processing Time

end = time.time() # end processing time
print("Tempo de processamento (s):",end - start)

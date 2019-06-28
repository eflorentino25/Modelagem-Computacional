import math
import os
import random
#-------------------------
n = 500 #Numero de moleculas
m = 3 #Posições em Z,X e Y
Caixa = 40
Moleculas = [[0] * m for i in range(n)] #Criação do array para posição das moleculas
#Moleculas[0] = [1,1,1]  #Localização Moleculas 1,2,3 ou r,g,b , até 9
#Moleculas[1] = [4,5,6]  #até 10
#Moleculas[2] = [1,4,4]  #até 5
#Inicializando as moléculas em posições aleatórias dentro da caixa.
for y in Moleculas:
    for position in range(m):
        if position == 0:
            y[position] = random.randint(0,Caixa) #X
        elif position == 1: 
            y[position] = random.randint(0,Caixa) #Y
        elif position == 2:
            y[position] = random.randint(0,Caixa) #Z
            
#Moleculas = [r,b,g]
Velocidades = [[0] * m for i in range(n)] #Criação do array para velocidades em X,Y,Z das moleculas
d = []     #Vetor das diferenças entre as posições 
Vet_un = []
All_Vet_un = []
Dir_For = []
Velocidade_ind = []

for i in range(0,m):
    d.append(0)
    Vet_un.append(0)
    All_Vet_un.append(0)
    Dir_For.append(0)
    Velocidade_ind.append(0)   
#Vet_un    = [0,0,0]
#All_Vet_un = [0,0,0]
#Dir_For = [0,0,0]
#Velocidade_ind = [0,0,0]
Resultantes = []
Result_Vet_un = []
All_Dir_For = []
All_Vel_Ab = []
#-------------------------
# Constantes:
 
M = 0.000039948
U_0 = 1 
R_0 = 1
filename = "Mol"
filename2 = "Vel"
filename3 = "Ace"
F = 0
Dist_real = 0 
check = 0
 
for time in range(1,100,1): 
    for a in Moleculas: 
        for y in Moleculas:
            if y != a:
                check = 1
                for position in range(m): 
                    d[position] = a[position] - y[position]
             
                for position in range(m):
                    Dist_real += math.pow(d[position],2)
                Dist_real = math.sqrt(Dist_real)
#                Dist_real = math.pow(d[0],2) + d[1]*d[1]+ d[2]*d[2]
           
                for position in range(m): 
                    Vet_un[position] += d[position]/Dist_real
#                Vet_un[0] = d[0]/Dist_real
#                Vet_un[1] = d[1]/Dist_real
#                Vet_un[2] = d[2]/Dist_real                    
#                X = X + Vet_un[0]
#                Y = Y + Vet_un[1]
#                Z = Z + Vet_un[2]
                F = F + (12*U_0/R_0) *(math.pow((R_0/Dist_real),13) - math.pow((R_0/Dist_real),7))
		#Loop a
        if check == 1:
            Result_Vet_un.append(Vet_un)
            Resultantes.append(F)
            F = 0	
            check = 0
    for laco1 in range(n):
        for laco2 in range(m):
            Dir_For[laco2] = Result_Vet_un[laco1][laco2] * Resultantes[laco1]
        All_Dir_For.append(Dir_For)
        
   
                      
#Cálculos acima são para Medir aceleração
    #"Atualizando a velocidade:
    for speed in range(n):
        for laco1 in range(m):
            Velocidades[speed][laco1] += All_Dir_For[speed][laco1]
            
#    print(Velocidades)
    
# Zerar Resultantes intermediarios para não ocupar memória.
    All_Dir_For =    []
    
    #"Atualizando a posição das moléculas. dS = dT * dV
    #Forçando a mudança de direção Caso ultrapasse os limites da caixa
    teste = 0
    for mol in range(n):
        for XYZ in range(m):
            if XYZ == 0:
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ] #Como Espaço = a(F) * dT(1)
                if teste > Caixa or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]
            elif XYZ == 1:
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ]
                if teste > Caixa or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]                
            elif XYZ == 2:
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ]
                if teste > Caixa or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]                
    V = 0 
    for mol in Velocidades:
        V += math.pow(mol[0],2) + math.pow(mol[0],2) + math.pow(mol[0],2)
    All_Vel_Ab.append(V)
        
    
    
            
            
            
            

#******************
#Abrir arquivos e gravar 500 posições X n iterações.
#******************
                
    os.chdir("D:\\UNIFESP\\ModComp\\Projeto5\\Arq_Mov")     
    c = filename + str(time)    
    file = open(c,'w')
    file.write(str(Moleculas)+"\n")
    file.close()
    
    os.chdir("D:\\UNIFESP\\ModComp\\Projeto5\\Vel")
    c = filename2 + str(time)    
    file = open(c,'w')
    file.write(str(Velocidades)+"\n")
    file.close() 
    
    
    os.chdir("D:\\UNIFESP\\ModComp\\Projeto5\\Ace")
    c = filename3 + str(time)    
    file = open(c,'w')
    file.write(str(Resultantes)+"\n")
    file.close()    

    # Zerar Resultantes intermediarios para não ocupar memória.
    Result_Vet_un = []    
    Resultantes = []  
    
    
os.chdir("D:\\UNIFESP\\ModComp\\Projeto5") #Pasta diferente para arquivo final.
file_final = open("Movimentos_totais.txt",'w')
filename4  = open("EnergiaCinetica.txt",'w')
for a in All_Vel_Ab:
    filename4.write(str(a)+' ')
#    print(a)

filename4.close()

os.chdir("D:\\UNIFESP\\ModComp\\Projeto5\\Arq_Mov")         
for filename in os.listdir("D:\\UNIFESP\\ModComp\\Projeto5\\Arq_Mov"):
    file = open(filename,'r')
    contents = file.read()
    for a in contents:
        if a in '0123456789. ':
            file_final.write(str(a))
        if a in ',[]' :
            file_final.write(' ')
    file.close()
    os.remove(filename)
file_final.close()

 

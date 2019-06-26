import math
import os

#-------------------------
n = 5 #Numero de moleculas
m = 3 #Posições em Z,X e Y
Moleculas = [[0] * m for i in range(n)] #Criação do array para posição das moleculas
Moleculas[0] = [1,1,1]  #Localização Moleculas 1,2,3 ou r,g,b , até 9
Moleculas[1] = [4,5,6]  #até 10
Moleculas[2] = [1,4,4]  #até 5
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

#-------------------------
# Constantes:
 
M = 0.000039948
U_0 = 1 
R_0 = 1
filename = "Mol"

F = 0
Dist_real = 0
 
for time in range(1,1000,1): 
    for a in Moleculas: 
        for y in Moleculas:
            if y != a:
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
                F = F + 12 *(math.pow((1/Dist_real),13) - math.pow((1/Dist_real),7))
		#Loop Y
        Result_Vet_un.append(Vet_un)
        Resultantes.append(F)
        F = 0
	#Loop a molecula	
        
	
	
#    print("\n",time,":",Resultantes)
    
#    print("\n Resultantes:\n",Result_Vet_un,"\n","Forças:",Resultantes,"\n",Dir_For)
    for laco1 in range(n):
        for laco2 in range(m):
#            print(Dir_For[laco2],"em>",laco2, Result_Vet_un[laco1][laco2],"em>",laco1,laco2,  Resultantes[laco1],"em>",laco1)
            Dir_For[laco2] = Result_Vet_un[laco1][laco2] * Resultantes[laco1]
#            print(Dir_For[laco2] )
        All_Dir_For.append(Dir_For)
        
# Zerar Resultantes intermediarios para não ocupar memória.
    Result_Vet_un = []    
    Resultantes = []  
    
#    All_Dir_For = []
#    Dir_For = []   
#    for i in range(0,m):
#        Dir_For.append(0)
              
        
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
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ]
                if teste > 9 or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]
            elif XYZ == 1:
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ]
                if teste > 10 or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]                
            elif XYZ == 2:
                teste = Moleculas[mol][XYZ] + Velocidades[mol][XYZ]
                if teste > 5 or teste < 0:
                    Velocidades[mol][XYZ] *= -1
                Moleculas[mol][XYZ] += Velocidades[mol][XYZ]             
    
#    print(time,":\n",Moleculas,"\n")
    
#******************
#Abrir arquivos e gravar 500 posições X n iterações.
#******************
    os.chdir("D:\\UNIFESP\\ModComp\\Projeto5\\Arq_Mov")     
    c = filename + str(time)    
#    print (c)
    file = open(c,'w')
    file.write(str(Moleculas)+"\n")
    file.close()
        
file_final = open("Movimentos_total.txt",'w')
for filename in os.listdir("D:\\UNIFESP\\ModComp\\Projeto5\\Arq_Mov"):
    file = open(filename,'r')
    contents = file.read()
    file_final.write(str(contents))
    file.close()
    os.remove(filename)
file_final.close()

 

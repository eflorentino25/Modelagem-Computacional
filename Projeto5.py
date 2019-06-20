import math


#-------------------------
r = [1,1,1]
b = [4,5,6]
g = [1,9,9]
Moleculas = [r,b,g]
r = [0,0,0]
Resultantes = []
Vet_un = []
All_Vet_un = [0,0,0]
Result_Vet_un = []
X  = 0
Y  = 0
Z  = 0 
Dir_For = [0,0,0]
All_Dir_For = []
Velocidade_ind = [0,0,0]
All_Velocidade = []
#-------------------------
 #Constantes:
 
 
 
M = 0.000039948
U_0 = 1 
R_0 = 1


F = 0
Dist_real = 0
 
for time in range(0,100000,1): 

for a in Moleculas: 
    for y in Moleculas:
        if y != a:
            r[0] = a[0] - y[0]
            r[1] = a[1] - y[1]
            r[2] = a[2] - y[2]
            Dist_real = math.pow(r[0],2) + r[1]*r[1]+ r[2]*r[2]
            Vet_un[0] = r[0]/Dist_real
            Vet_un[1] = r[1]/Dist_real
            Vet_un[2] = r[2]/Dist_real
            X = X + Vet_un[0]
            Y = Y + Vet_un[1]
            Z = Z + Vet_un[2]
#            print(Dist_real,r)
            Dist_real = math.sqrt(Dist_real)
            F = F + 12 *(math.pow((1/Dist_real),13) - math.pow((1/Dist_real),7))
            
    Resultantes.append(F)
    All_Vet_un[0] = X
    All_Vet_un[1] = Y
    All_Vet_un[2] = Z
    Result_Vet_un.append(All_Vet_un)
    F = 0
    X = Y = Z = 0

print(Resultantes)



for r in range(0,len(Result_Vet_un)):
    for i in range(0,2):
        Dir_For[i] = Result_Vet_un[r][i] * Resultantes[r]
    All_Dir_For.append(Dir_For)


#Calculos acima são para Medir aceleração


#A Criar:
#    
#    Método de Euler -> Integração
#    Deslocamento




















 
 
 

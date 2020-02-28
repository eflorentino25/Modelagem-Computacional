import numpy
import matplotlib.pyplot as plt
import pandas as pd

G_ALL = []
C_ALL = []
P_ALL = []
F_ALL = []
K_ALL = []
x     = []
     

##class MyObj(object):
##
##    def __init__(self, num_loops):
##        self.count = num_loops
##
##    def go(self):
##        for i in range(self.count):
##            pdb.set_trace()
##            print(i)
##        return
##
##if __name__ == '__main__':
##    MyObj(5).go()

def realfitness(ESP,GRAPH):
# Calculating the fitness value of each solution in the current population.
# The fitness function calculates the sum of products between each input and its corresponding weight.
    G= 5000      #Grama
    C= 1         #Condor
    P= 1         #PITON
    F= 2         #filhote de cabra
    K= 2         #Capivara
    
##    print('\n Sequência de parametros', ESP)
##    ##MT_K =0.4        ESP[0] #Taxas de mortalidade 
##    ##MT_F =0.4        ESP[1]
##    ##MT_C =0.4        ESP[2]
##    ##MT_P =0.4        ESP[3]
##    ##Alfa_Prod_G =0.4 ESP[4]  # Taxa de crescimento do produtor (grama)
##    ##Cons_P_K = 0.2   ESP[5]##Constantes de consumo. 
##    ##Cons_P_F = 0.2   ESP[6] 
##    ##Cons_C_F = 0.2   ESP[7]
##    ##Cons_C_P = 0.2   ESP[8]
##    ##Cons_C_K = 0.2   ESP[9]
##    ##Cons_K_G = 0.2   ESP[10]
##    ##Cons_F_G = 0.2   ESP[11]
##    ##Cons_K_P = 0.3   ESP[12]#Taxas de Dano
##    ##Cons_K_C = 0.3   ESP[13]
##    ##Cons_F_P = 0.3   ESP[14]
##    ##Cons_F_C = 0.3   ESP[15]
##    ##Cons_F_C = 0.3   ESP[16] 
    

    #Limite de crescimento da grama
    Lim_Prod 	= 10000
    fitness 	= 0
    c_top = 9999
    Fitness_ref = 0
    #//Taxa de crescimento da grama - QT de Filhotes de cabra e capivara * constante de consumograma.
##    pdb.set_trace() #é o breakpoint do python.
##    if GRAPH == 'X':

    for i in range(0,100000,1):       
        Beta=(1- G / Lim_Prod )
        D_G = G *((ESP[4] * Beta) - (ESP[10] * K + ESP[11] * F))
        D_K = K *(-ESP[0] + ESP[17] * G - ESP[12] * P - ESP[13] * C)
        D_F = F *(-ESP[1] + ESP[18] * G - ESP[14] * P - ESP[15] * C)
        D_C = C *(-ESP[2] + ESP[8]  * P + ESP[7]  * F + ESP[9]  * K)
        D_P = P *(-ESP[3] + ESP[6]  * F + ESP[5]  * K - ESP[16] * C)

        G = G + (D_G * 0.01)
        C = C + (D_C * 0.01)
        P = P + (D_P * 0.01)
        F = F + (D_F * 0.01)
        K = K + (D_K * 0.01)
        
        if G <0:
            G=0
        if C <0:
            C=0
        if P <0:
            P=0
        if F <0:
            F=0
        if K <0:
            K=0
            
        if GRAPH == 'X':
            G_ALL.append(int(G))
            C_ALL.append(int(C))
            P_ALL.append(int(P))
            F_ALL.append(int(F))
            K_ALL.append(int(K))

     

        if G > 0 : #or K > 0 or F > 0 or P>0 or C>0 : # and  P > 0 and C > 0):
            fitness += 0.5 #Maior prioridade
            if K > 0:
                fitness += 0.2  #Segunda prioridade
                if F > 0:
                    fitness += 0.2  #Segunda prioridade
                    if P > 0:
                        fitness += 0.05
                        if C > 0:
                            fitness += 0.1 #Menor prioridade
                            if(fitness >= c_top):
                                fitness = fitness * 0.1
                                Fitness_ref += fitness
                                fitness = 0
                                if (Fitness_ref >= 9998):
                                    Fitness_ref = c_top
                                    break # Se valor testado acima de 
                        else:
                            Fitness_ref = Fitness_ref + (fitness * 0.1) 
                            break #Se P e C <= 0   
                    else:
                        Fitness_ref = Fitness_ref + (fitness * 0.1) 
                        break #Se P e C <= 0  
                else:
                    Fitness_ref = Fitness_ref + (fitness * 0.1) 
                    break #Se P e C <= 0  
            else:
                Fitness_ref = Fitness_ref + (fitness * 0.1)
                break #Se F e K <= 0           
        else:
            Fitness_ref = Fitness_ref + (fitness * 0.1)
            break #Se Grama <= 0 
            
#se sair do loop sem retornar o fitness
   
    
    if GRAPH == 'X':
        print('Tamanho pos Grama:',len(G_ALL))
        print('Tamanho pos Condor:',len(C_ALL))
        print('Tamanho pos Piton:',len(P_ALL))
        n = 0
        for num in range(len(G_ALL)):
            n+=0.1
            x.append(n)
        
        print('Tamanho pos tempo:',len(x))

        df = pd.DataFrame({'x': x, 'Grama': G_ALL, 'Condor': C_ALL, 'Piton': P_ALL, 'Filhote': F_ALL, 'Coala': K_ALL})

        #
        plt.style.use('seaborn-darkgrid')
        palette = plt.get_cmap('Set1')

        num=0
        for column in df.drop('x', axis=1):
            num+=1
         
            # Find the right spot on the plot
            plt.subplot(3,3, num)
         
            # plot every groups, but discreet
            for v in df.drop('x', axis=1):
                plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
         
            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), label=column)
         
            # Same limits for everybody!
            plt.xlim(0,max(x)+1)
            plt.ylim(min(df[column]),max(df[column]))
         
            # Not ticks everywhere
            if num in range(7) :
                plt.tick_params(labelbottom=False)
            if num not in [1,4,7] :
                plt.tick_params(labelleft=False)
         
            # Add title
            plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )
            plt.suptitle("Quantidade", fontsize=12, fontweight=0, color='black', style='italic', y=1.02)
         #
        # Axis title
        plt.text(0.5, 0.02, 'Tempo', ha='center', va='center')
        plt.text(0.06, 0.5, 'Quant', ha='left', va='center', rotation='vertical')
        
        plt.plot('x', 'G_ALL', data=df, color='blue')
        plt.plot('x', 'C_ALL', data=df, color='green')
        plt.plot('x', 'P_ALL', data=df, color='red')
        plt.plot('x', 'F_ALL', data=df, color='yellow')
        plt.plot('x', 'K_ALL', data=df, color='orange')
    
    else:
       
        return Fitness_ref


def select_mating_pool(pop, fitness, num_parents):
    # Selecting the BEST individuals in the current generation as parents for producing the offspring of the next generation.

    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        if parent_num > 10:
##          Selecting the WORST individuals in the current generation to substitute.
            pop_siz = (1,19)
            
            randomics = numpy.random.uniform(low=0, high=1.0, size=pop_siz)
            
            max_fitness_idx = numpy.where(fitness == numpy.max(fitness))

            max_fitness_idx = max_fitness_idx[0][0]
             
            parents[parent_num, :] = randomics[0,:]
            
            fitness[max_fitness_idx] = -99999999999

        else:
##          Selecting the BEST individuals to become parents for the next generation
            max_fitness_idx = numpy.where(fitness == numpy.max(fitness))

            max_fitness_idx = max_fitness_idx[0][0]

            parents[parent_num, :] = pop[max_fitness_idx, :]

            fitness[max_fitness_idx] = -99999999999

    return parents

def cal_pop_fitness(pop):
    index = 0
    ESP_ALL = pop
    fitness = numpy.zeros((20))
    fitness.astype(numpy.int64)
    maximo = 0
    for ESP in ESP_ALL:
        retorno = realfitness(ESP,'N')
        fitness[index] = retorno
        index += 1
        maximo = numpy.max(fitness)
##        if maximo >1000 and index > 19:
##            print()
    return fitness

     

def crossover(parents, offspring_size):
     offspring = numpy.empty(offspring_size)
     # The point at which crossover takes place between two parents. Usually, it is at the center.
     crossover_point = numpy.uint8(offspring_size[1]/2)
     for k in range(offspring_size[0]):
         # Index of the first parent to mate.
         parent1_idx = k%parents.shape[0]
         # Index of the second parent to mate.
         parent2_idx = (k+1)%parents.shape[0]
         # The new offspring will have its first half of its genes taken from the first parent.
         offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
         # The new offspring will have its second half of its genes taken from the second parent.
         offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
     return offspring

def mutation(offspring_crossover):

    # Mutation changes a single gene in each offspring randomly.

    for idx in range(offspring_crossover.shape[0]):

        # The random value to be added to the gene.

        random_value = numpy.random.uniform(0, 1.0, 1)

        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value

    return offspring_crossover


##*---------------MAIN-------------------------------
sol_per_pop = 20
### Inputs of the equation.

### Number of the weights we are looking to optimize.
num_weights = 19
### Defining the population size.

pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.

###Creating the initial population.

new_population = numpy.random.uniform(low=0, high=10.0, size=pop_size)

num_generations = 0

num_parents_mating = 19

fitness_gen = cal_pop_fitness(new_population)

Sol_max = new_population
Fit_max = fitness_gen

f_max  = numpy.max(fitness_gen)
ft_max = numpy.max(Fit_max)

##for generation in range(num_generations):
print('Maior inicial: ',numpy.max(fitness_gen))

while True:
##    print('O melhor da geração',numpy.max(fitness))
    # Measuring the fitness of each chromosome in the population.
    fitness_gen = cal_pop_fitness(new_population)
    f_max  = numpy.max(fitness_gen)

    # Saving the best result in separate variable. 
    if f_max > ft_max:        
        Sol_max = new_population
        Fit_max = fitness_gen
        print('Maximo Gen ',num_generations,':', numpy.max(Fit_max))
        ft_max = numpy.max(Fit_max)
    #Breaking when result > 1000 or another number we choose
    best_match = numpy.max(Fit_max)
    if best_match >= 9999:
        break

    # Selecting the best parents in the population for mating.
    parents = select_mating_pool(new_population, fitness_gen, 
                                       num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = crossover(parents,
                            offspring_size=(pop_size[0]-parents.shape[0],
                                            num_weights))
 
    # Adding some variations to the offsrping using mutation.
    offspring_mutation = mutation(offspring_crossover)
    
    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
    
    # The best result in the current iteration.
    best_match_idx = numpy.where(fitness_gen == numpy.max(fitness_gen))
        
    num_generations += 1   

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness_gen = cal_pop_fitness(new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness_gen == numpy.max(fitness_gen))


if numpy.max(fitness_gen) > numpy.max(Fit_max):
    Sol_max = new_population
    Fit_max = fitness_gen

##--------------Gráfico-------------------------    

#Lista de QT das especies por tempo.
best_match_idx = numpy.where(fitness_gen == numpy.max(fitness_gen))
Array_final = Sol_max[best_match_idx[0],:]
bk = 0
for Array in Array_final:
    if bk>0:
        break
    realfitness(Array,'X')
    bk += 1
    


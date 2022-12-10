#!/usr/bin/env python
# coding: utf-8

# In[402]:


import random

#================INPUT OPERATIONS===================#
file = open('input.txt','r')

lines = file.readlines()

file.close()

for i in range(len(lines)):
    
    lines[i]=lines[i].strip()
    

N = int(lines[0][0])
T = int(lines[0][1:])
lines.pop(0)


list = [] #list of players with [['player_1',R1],....['player_N',RN]] 
for i in range(len(lines)):
    
    tmp = lines[i].split(' ')
    list.append([tmp[0],int(tmp[1])])
    

    
def string_to_list(string):
    lst = []
    for i in range(len(string)):
        lst.append(string[i])
        
    return lst


def list_to_string(lst):
    string = ''
    for i in range(len(lst)):
        string+=lst[i]
        
    return string


        

#================GENETIC ALGO FUNCTIONS===================#
def fitness_check(comb): #THIS RETURNS THE 'FARNESS' FROM T RUNS, MEANING HAVING 0 IS BEST
                         #comb = string combination of 1s and 0s
    sum = 0
    
    for i in range(0,N):
        
        if comb[i]=='1':
            sum+=list[i][1]
            
    away = abs(T-sum)
    
    return away


def selection(pop): 
    
    new_pop = []
    
    for i in range(0,len(pop)):
        
        if fitness_check(pop[i])<=50:
            
            new_pop.append(pop[i])
    
    if len(new_pop)<2: #IF ONLY ONE OR NONE OF THE SAMPLES ARE GOOD, THEN PASS ON OLD POPULATION
        return pop
            
    return new_pop


def crossover_between_parents(p1,p2):
    
    first_parent = string_to_list(p1)
    second_parent = string_to_list(p2)
                                        
    ran = random.randint(1,N-1)            
    first_parent[ran:N],second_parent[ran:N] = second_parent[ran:N],first_parent[ran:N]            
            
    off1 = list_to_string(first_parent)
    off2 = list_to_string(second_parent)

    return [off1,off2]
    

def crossover(pop):
    
    offsprings = []
    
    if len(pop)%2==0:
        for i in range(0,len(pop),2):            
            offsprings+=crossover_between_parents(pop[i],pop[i+1])
            
    else:        
        for i in range(0,len(pop)-1,2):            
            offsprings+=crossover_between_parents(pop[i],pop[i+1])
            
        offsprings+=crossover_between_parents(pop[-2],pop[-1]) #crossing over last index and the index before that if ODD pop.
                    
    
    return offsprings
            
def mutation(pop):
                    
    for i in range(0,len(pop)):
        
        mutate_probabilty = random.choice([0,1])
        
        if mutate_probabilty==1:  #50% chance of an offspring being mutated.
            
            tmp = string_to_list(pop[i])            
                
            ran = random.randint(0,N-1)  
            if tmp[ran]=='1':        
                tmp[ran]='0'        
            else:
                tmp[ran]='1'
        
            mutated = list_to_string(tmp)
    
            pop[i]=mutated
                 
    return pop




#================GENERATING POPULATION===================#
pop=[]
for i in range(40): #CREATING POPULATION OF 40 SAMPLES
    tmp = ''
    for j in range(0,N):        
        tmp+=str(random.randint(0,1))
    pop.append(tmp)
    

    
#================RUNNING GA ON POPULATION 20000 TIMES===================#   

answer = None #for storing highest possible fitness string
best_score = float('inf')  #for storing highest fitness value 

best_found = False

for i in range(20000):
                   
    if best_found==True:
        break        
    
    #keeping strings with sum of 280-380 which is having 'farness' or fitness of 50 or less.
    #IF ONLY ONE OR NONE OF THE SAMPLES ARE GOOD, THEN PASS ON OLD POPULATION
    #selection
    pop = selection(pop)
            
    #crossing over
    pop = crossover(pop)
                
    
    #mutation
    pop = mutation(pop)
        
    #fitness_checking  
    for j in range(len(pop)):
        
        score = fitness_check(pop[j]) #lower is better with 0 being the best.        
        
        if score==0:  #best fitness ( score=0 ) is found.
            answer = pop[j]
            best_score = score
            best_found=True
            break
            
        elif score<best_score: # highest possible fitness.
            best_score = score
            answer = pop[j] #highest possible fitness string stored.
                       

output_players = []
for j in range(len(list)):
    output_players.append(list[j][0])
print(output_players)           
if best_found==True:
    print(answer)
else:
    print(-1)
       


#print(best_score,answer)
#for printing (highest_possible_fitness obtained and string)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





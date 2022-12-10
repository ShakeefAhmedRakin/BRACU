#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
import math

def alpha_beta(depth, index, mode,leaves, alpha, beta):

    if depth!=3:
        
        if mode=='MAX':
      
            current_best = float('-inf') #currently stored best possible value
                
            # checking n*2+0[i=0] node(left child) and n*2+1[i=1] node(right child)
            i = 0 
            while i!=2:
                       
                # recurring for childs (left first) until terminal.
                pot_new_best = alpha_beta(depth+1,index*2+i,'MIN', leaves,alpha,beta)
                current_best = max(current_best, pot_new_best)
                alpha = max(alpha, current_best)
                i+=1
 
                if alpha >= beta:
                    break
          
            return current_best
      
        elif mode=='MIN':
        
            current_best = float('inf')
        
            i = 0 
            while i!=2:
                
                
                pot_new_best = alpha_beta(depth+1,index*2+i,'MAX',leaves,alpha,beta)
                current_best = min(current_best, pot_new_best)
                beta = min(beta, current_best)
                i+=1
 
                if alpha >= beta:
                    break
          
            return current_best
        
    else:
        
        terminal_value = leaves[index]
        
        return terminal_value
 
    
      

#------------------------------------------------------------------------------#


user_id = input("Enter your student ID:")

min_point = int(user_id[4])

point_win = int(user_id[8:5:-1])

max_point = math.ceil(point_win*1.5)

S = int(user_id[3])

def who_won(score):
    
    if score>=point_win:
        
        return 'The Winner is Optimus'
    
    else:
        
        return 'The Winner is Megatron'

#TASK - 1#

print('----------------TASK 1-------------------')
leaves = []
 
for i in range(8):    
    leaves.append(random.randint(min_point,max_point))
        
    
score = alpha_beta(0, 0, 'MAX', leaves, float('-inf'), float('inf'))

print('Generated 8 random points between the minimum and maximum point limits:',leaves)
print('Total points to win:',point_win)
print('Achieved point by applying alpha-beta pruning =',score)
print(who_won(score))




#Task - 2#
print('----------------TASK 2-------------------')

score_list = []

for i in range(S):
    random.shuffle(leaves)
    score_list.append(alpha_beta(0, 0, 'MAX', leaves, float('-inf'), float('inf')))

win_times = 0

for i in score_list:
    
    if who_won(i)=='The Winner is Optimus':
        win_times +=1

print('After the shuffle:')
print('List of all points values from each shuffle:',score_list)
print('The maximum value of all shuffles:',max(score_list))            
print('Won',win_times,'times out of',str(S),'number of shuffles')



print('-----------------------------------------')     


# In[ ]:





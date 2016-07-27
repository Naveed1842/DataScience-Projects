
#!/usr/bin/python
# -*- coding: utf-8 -*- 


import load
import json
from math import sqrt

##Calculate similarity using Euclidean distance
def sim_euc(prefs, p1, p2):
    
    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Add up the squares of all the differences
    #print(si)
    dis = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in si])
    return round(1 / (1 + (dis)),2)

##Calculate similarity between two person using Manhattan distance
def sim_man(prefs,p1,p2):
    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    #print(si)
    dis = sum([abs(prefs[p1][item] - prefs[p2][item]) for item in si] )
    #print(dis)
    return round(1 / (1 + sqrt(dis)),2) 

##Calculate similiarity using Lmax
def sim_Lmax(prefs,p1,p2):
    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    #print(si)
    dis = max([abs(prefs[p1][item] - prefs[p2][item]) for item in si] )
    #print(dis)
    return round(1 / (1 + sqrt(dis)),2) 

##similiarity calculation using pearson correlation
def sim_pearson(prefs,p1,p2):
    #Get the list of shared_items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    #if they have no ratings in common,return 0
    if len(si)==0:
         return 0  
    #Add up all the preferences
    sum1=sum([prefs[p1][it] for it in si])  
    sum2=sum([prefs[p2][it] for it in si])

    #sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    #sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #calculate pearson score
    n=len(si)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return round(r,2)

### similarity calculation using demographic information
def sim_demographic(prefs,p1,p2):
    
    ##Calculating Euclidean similarity based on past similar movies W1=0.5  
    s1=sim_euc_dem(prefs,p1,p2)
    w1=0.1
    
    ### calculating Age group similarity W2=0.2
    s2=sim_agegroup(prefs,p1,p2)
    w2=0.4
    
    ### Caclculating Gender similarity   W3=0.2
    s3=sim_gender(prefs,p1,p2)
    w3=0.4

    ###Calculating Occupatinal similarity W4=0.10
    s4=sim_occupation(prefs,p1,p2)
    w4=0.1
    
    return s1*w1+s2*w2+s3*w3+s4*w4

def sim_euc_dem(prefs,p1,p2):
    #Assigned 0.5 wait to past movies 
    si = {}
    for item in prefs[p1]['movies']:
        if item in prefs[p2]['movies']:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Add up the squares of all the differences
    #print(si)
    dis = sum([pow(prefs[p1]['movies'][item] - prefs[p2]['movies'][item], 2) for item in si])
    return round(1 / (1 + sqrt(dis)),2)

def sim_agegroup(prefs,p1,p2):
     #Assigned 0.2 weight to agegroup
    if((0<=prefs[p1]['age']-prefs[p2]['age'])<=8):
        return 1
    elif(8<(prefs[p1]['age']-prefs[p2]['age'])<=16):
        return 0.8
    elif(16<(prefs[p1]['age']-prefs[p2]['age'])<=24):
        return 0.6
    elif(24<(prefs[p1]['age']-prefs[p2]['age'])<=32):
       return 0.4    
    else:
       return 0.2    

def sim_gender(prefs,p1,p2):
    #Assiging 0.2 weight to gender
    if(prefs[p1]['gender']==prefs[p2]['gender']):
        return 1

    else: 
        return 0.75
def sim_occupation(prefs,p1,p2):
    ##Assigned 0.10 weight to occupation
    g1={'administrator':1,'doctor':1,'educator':1,'executive':1,'healthcare':1,'librarian':1,'none':1,'other':1}
    g2={'artist':1,'entertainment':1,'homemaker':1,'marketing':1,'none':1,'other':1,'salesman':1,'student':1,'writer':1}
    g3={'engineer':1,'programmer':1,'none':1,'other':1,'scientist':1,'technician':1}
    g4={'retired':1,'none':1,'other':1}
    
    if(prefs[p1]['occupation']==prefs[p2]['occupation']):
        return 1

    else:
        return 0.5

        
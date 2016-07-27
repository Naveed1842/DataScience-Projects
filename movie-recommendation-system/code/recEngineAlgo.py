#!/usr/bin/python
# -*- coding: utf-8 -*- 


import load
import json
import similarity
from math import sqrt


### top K user algorithm
def getRecommendation(j,prefs,movies,k,similarity):

    
    ##Calculating similarity matrix
    simDic={}
    for person in prefs:
        simDic.setdefault(person,{})
        for other in prefs:
            if other!=person:
                sim=similarity(prefs,person,other)
                simDic[person][other]=sim
             
    rec={}
    i=1
    
    ##Now calculating recommendation for each person for each movie they didn't see
    for person in prefs:
        print(i)
        rec.setdefault(person,{})
        topCritics=[]
        print("calculating for person",i)
     
        for other in prefs:
            if other !=person:
                 
                sim=simDic[person][other]
                topCritics.append((sim,other))
        topCritics.sort()
        topCritics.reverse()
      
        for movie in movies:
            if movie not in prefs[person]:
                
                count=0
                sumTopKUsersRating=0
                sumSimilarity=0

                for user in topCritics:     
                                
                    if movie in prefs[user[1]]:
                        
                        
                        sumTopKUsersRating=sumTopKUsersRating+user[0]*prefs[user[1]][movie]  #sum(similarity*rating)
                        sumSimilarity=sumSimilarity + user[0]
                        count=count+1
                        
                    if(count==k):
                        break

                if(count!=0 and sumSimilarity!=0):        
                    rec[person][movie]=round(sumTopKUsersRating/sumSimilarity,2)
                    
        i=i+1            
    with open('./Datastore/rec_'+ similarity.__name__+ '_' + str(k) + '_'+ str(j)+'.json','w') as fp:
        json.dump(rec,fp)                

###############################################Testing############################################
#getRatings(load.readPrefs('prefsTrain.json'),'553')
#topCritics(load.readPrefs('prefsTrain.json'),'553')
#getRecommendation(load.readPrefs('prefsTrain1.json'),load.readPrefs('simDic.json'),load.readPrefs('movies.json'),100)
#getRecommendation(1,load.readPrefs('./DataStore/prefsTrain1.json'),load.readPrefs('./Datastore/movies_100K.json'),32,similarity.sim_euc)

#print(s)
#simStorage(load.readPrefs('prefsTrain1.json'))
import load
import json
import similarity
from math import sqrt

def avgMovieRating(movies,prefs):
	movieAvg={}
	for movie in movies:
		movieAvg.setdefault(movie,0)
		movieRating=0
		movieReach=0
		for person in prefs:
			if movie in prefs[person]:
				movieRating=movieRating+prefs[person][movie]
				movieReach=movieReach+1
		if(movieReach!=0):
			movieAvg[movie]=round(movieRating/movieReach,0)

	with open('./Datastore/movieAvg1.json','w') as fp:
	    data=json.dump(movieAvg,fp)    

def getRecommendation(prefs,movieAvg):
	rec={}
	i=1
	for person in prefs:
		rec.setdefault(person,{})
		for movie in movieAvg:
			if movie not in prefs[person]:
				rec[person][movie]=movieAvg[movie]
		i=i+1
	with open('./Datastore/recAvgTrain1.json','w') as fp:
		data=json.dump(rec,fp)




#############################Testing############################################
#avgMovieRating(load.readPrefs('./Datastore/movies.json'),load.readPrefs('./Datastore/prefsTrain1.json'))	 
#getRecommendation(load.readPrefs('./Datastore/prefsTrain1.json'),load.readPrefs('./Datastore/movieAvg1.json'))    
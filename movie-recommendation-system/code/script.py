# -*- coding: utf-8 -*-

#reading raw files and inserting content into dictionary
import load
import recEngineBaseAlgo
import recEngineAlgo
import recEngineDemoAlgo
import mad
import similarity
import json

###Load all the K folds for training and testing
'''
print("Loading all the K folds for training and testing")
load.loadData()
'''
def test():
	result={}
	func={'sim_euc':similarity.sim_euc,'sim_man':similarity.sim_man,'sim_Lmax':similarity.sim_Lmax}
	for fun in func: #For all three Metrics
		for k in [10,50,100]: #check for three different k values(Handpicked)
			result.setdefault(fun,{})
			for i in [1,2,3,4,5]:# 5 fold cross validation
				madScore=0
				madlist=[]
				print("Running",i,"Validation for function",fun,"k value is",k)
				#print("In script")
				#print('./Datastore/rec_'+str(fun)+ '_'+str(k) + '_'+ str(i)+'.json')
				recEngineAlgo.getRecommendation(i,load.readPrefs('./Datastore/prefsTrain'+str(i)+'.json'),load.readPrefs('./Datastore/movies.json'),k,func[fun])
				madScore=mad.mad(load.readPrefs('./Datastore/rec_'+str(fun)+ '_'+str(k) + '_'+ str(i)+'.json'),load.readPrefs('./Datastore/prefsTest'+str(i)+'.json'))	
				print("Madscore for",i,"validation for function",fun,"with k value",k,"is",madScore)
				madlist.append(madScore)

			for item in madlist: #Taking average Mad
				madScore=madScore+item
				print("Final MadScore for func:",str(fun),"and k:",k,"is:",round(madScore/5,2))
			result[fun][k]=round(madScore/5,2)
			print(result)
	
	with open('./Datastore/result.json','w') as fp: #storing the result in dictionary
		json.dump(result,fp)

def run(similarity,k):
	#5 fold cross validation
	madlist=[]
	for i in [1,2,3,4,5]:
		print("Running",i,"Validation for function",similarity.__name__,"k value is",k)
		recEngineAlgo.getRecommendation(i,load.readPrefs('./Datastore/prefsTrain'+str(i)+'.json'),load.readPrefs('./Datastore/movies.json'),k,similarity)
		#recEngineDemoAlgo.getRecommendation(i,load.readPrefs('./Datastore/prefsTrain_demographic.json'),load.readPrefs('./Datastore/movies.json'),k,similarity)
		#recEngineDemoAlgo.getRecommendation(i,load.readPrefs('./Datastore/prefsTrain'+str(i)+'.json'),load.readPrefs('./Datastore/movies.json'),k,similarity)
		#madScore=mad.mad(load.readPrefs('./Datastore/rec_'+similarity.__name__+ '_'+str(k) + '_'+ str(i)+'.json'),load.readPrefs('./Datastore/prefsTest'+str(i)+'.json'))	
		#madlist.append(madScore)				


#################################Testing#################################################################################
#test()	
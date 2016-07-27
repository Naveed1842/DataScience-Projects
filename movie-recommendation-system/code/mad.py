#!/usr/bin/python
# -*- coding: utf-8 -*- 


import load
import json
from math import sqrt

##Calculate Median Absolute difference

def mad(rec,prefsTest):
	madScore=0
	rij=0
	sum_total=0
	sum_rij=0
	for person in rec:

		for movies in rec[person]:
			if person in prefsTest:
				if movies in prefsTest[person]:
					rij=1
					sum_rij=sum_rij+rij
					sum_total=sum_total+rij*abs(rec[person][movies]-prefsTest[person][movies])
	if(sum_rij!=0):	
		madScore=madScore+round(sum_total/sum_rij,4)
	return madScore		
	
def mad_personal(rec,prefsTest,person):
	madScore=0
	rij=0
	sum_total=0
	sum_rij=0
	for movies in rec[person]:
		if person in prefsTest:
			if movies in prefsTest[person]:
				rij=1
				sum_rij=sum_rij+1
				sum_total=sum_total+rij*abs(rec[person][movies]-prefsTest[person][movies])
	if(sum_rij!=0):
		madScore=madScore+round(sum_total/sum_rij,4)
	return madScore			
############################Testing###################################################
#print(mad(load.readPrefs('./Datastore/sim_Lmax/rec_sim_Lmax_100_1.json'),load.readPrefs('./Datastore/prefsTest1.json')))
#print(mad_personal(load.readPrefs('./Datastore/sim_euc/rec_sim_euc_10_1.json'),load.readPrefs('./Datastore/prefsTest1.json'),'126'))
#print(mad(load.readPrefs('./Datastore/recAvgTrain2.json'),load.readPrefs('./Datastore/prefsTest2.json')))
#print(mad(load.readPrefs('./Datastore/rec_sim_euc_20_1.json'),load.readPrefs('./Datastore/prefsTest1.json')))
#print(mad(load.readPrefs('./Datastore/sim_demo/sim_demo2/rec_sim_demographic_30_1.json'),load.readPrefs('./Datastore/prefsTest1.json')))
print(mad(load.readPrefs('./Datastore/rec_sim_euc_32_1.json'),load.readPrefs('./Datastore/prefsTest1.json')))
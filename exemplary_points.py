# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:26:36 2016

Choose user-dependent exemplary points
    - 1 exemplary point per letter
    -> Total 10 exemplary points per person
    
@author: hjsong
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle
import knn_dtw_class as dtw
import time

def filter_and_getExemplaries(shouldFilter=True, shouldSave=True)

    all_exemplaries = {} #key = u_idx, value = exemplaries 
                        # exemplaries = dictionary with key=letter, value=data point (i.e. time series)
    #Read user data
    #u_idx=1 #Make sure to change data_userX variable name
    for u_idx in range(1,11):
        print "u_idx: ", u_idx
        user_labels = pickle.load(open("data/data_noID/user"+ str(u_idx)+"_labels.p", "rb"))
        user_data = pickle.load(open("data/data_noID/user"+ str(u_idx)+"_data.p", "rb"))
    
        m = dtw.KnnDtw();
        exemplaries = {}
        for letter_idx in range(1,11):
        #for letter_idx in range(10,11):    
            letter_data = user_data[10*(letter_idx-1):10*letter_idx]
            letter_labels = user_labels[10*(letter_idx-1):10*letter_idx]
            label = letter_labels[0]
            n = len(letter_data)
            
            s = time.time()
            dmtx = np.zeros((n,n));
            for i in range(len(letter_data)-1):
                for j in range(i+1, len(letter_data)):
                    d = m._dtw_distance(letter_data[i], letter_data[j])
                    dmtx[i][j] = d
                    dmtx[j][i] = d
            e = time.time()
            print 'Pairwise distance calculation for a user took : %.3f'%(e-s)
            
            dsums = dmtx.sum(axis=0)
            print '\n\n\nletter: ' + label
            plt.plot(dsums)
            plt.show()
            
            mean = dsums.mean()
            std = dsums.std()
            outliers = [];
            min_dist = float('inf')
            arg_min = None
            for i in range(len(dsums)):
                if (dsums[i] < mean-2*std or mean+2*std < dsums[i]):
                    outliers.append(i)
                    dsums[i] = float('inf')
                elif dsums[i] < min_dist:
                    min_dist = dsums[i]
                    arg_min = i
            exemplaries[label] = letter_data[arg_min] #exemplary tseries for this letter
            #If needed to filter out the outliers from letter_data
            if len(outliers) >0 :
                print "outliers are found: ", outliers
                
            if shouldFilter: 
                for outlier in outliers:
                    letter_data.pop(outlier)
                    letter_labels.pop(outlier)
                if shouldSave:
                    pickle.dump(letter_data, open('data/filtered/dump/' + str(u_idx) + "_" + str(label) + "_data.p", "wb"))
                    pickle.dump(letter_labels, open('data/filtered/dump/' + str(u_idx)+ "_"+ str(label) + "_labels.p", "wb"))
            
            
        #end of letter loop    
        all_exemplaries[u_idx] = exemplaries
    #end of u_idx loop
    pickle.dump(all_exemplaries, open('data/filtered/exemplaries.p','wb'))
    return all_exemplaries


def getExemplariesExcept(u_idx):
    all_exemplaries = pickle.load(open('data/filtered/exemplaries.p','rb'))
    concise = {}
    letters = ['O' ,'I', 'J', 'L', 'Z', 'S', 'V', 'T', 'X', 'B']

    for letter in letters:
        concise[letter] = []
    
    for user_idx, user_dict in all_exemplaries.iteritems():
        if user_idx == u_idx: continue
        for letter in letters:
            concise[letter].append(user_dict[letter])
            
    exemplary_trainX = []
    exemplary_trainY = []
    for label, list_exemplaries in concise.iteritems():
        for exemplary in list_exemplaries:
            exemplary_trainX.append(exemplary)
            exemplary_trainY.append(label)
    return (exemplary_trainX,exemplary_trainY)
        

    
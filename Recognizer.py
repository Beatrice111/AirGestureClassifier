# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:28:56 2016

@author: hjsong
"""
import pickle 
import knn_dtw_class as dtw
import numpy as np

class Recognizer(object):
    """
    Uses exemplary points from the training data to make predictions on the test data
    """
    def __init__(self):
        self.sample_rate = 10
        self.training_x = pickle.load(open('data/filtered/exemplary_trainX.p','rb'))
        self.training_y = pickle.load(open('data/filtered/exemplary_trainY.p','rb'))
        self.m = dtw.KnnDtw()
        self.m.fit(self.training_x, self.training_y)
        
    
    def preprocess(self,testing_pt):
        d = np.array(testing_pt)
        # only extract ax, ay out of the signals
        
        l, _ = d.shape
        if l < self.sample_rate:
            d = np.mean(d,axis=0).reshape(-1,2)
        else: 
            new_l = (l/self.sample_rate)*self.sample_rate
            remaining_d = d[new_l:, :]
            d = d[:new_l, :]
            d = np.mean(d.reshape(-1,self.sample_rate,2), axis = 1)
            if new_l != 1:
                d = np.vstack((d, np.mean(remaining_d, axis = 0)))
        # scale the data to be in range [-1,1]
        d = d / np.amax(np.abs(d), axis = 0)
        return d
                
        
    def predict_one(self,testing_pt):
        """
        Arguments
        ----------
            testing_x: a list of points to predict
        
        
        Returns
        -------
            a list of predicted letters
        """
        preprocessed = self.preprocess(testing_pt)
        return  self.m.predict([preprocessed])[0]
  



    
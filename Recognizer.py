# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:28:56 2016

@author: hjsong
"""
import pickle 
import knn_dtw_class as dtw
import numpy as np
from preprocess import preprocess

class Recognizer(object):
    """
    Uses exemplary points from the training data to make predictions on the test data
    """
    def __init__(self, sample_rate = 10):
        self.sample_rate = sample_rate
        self.training_x = pickle.load(open('data/exemplary_trainX.p','rb'))
        self.training_y = pickle.load(open('data/exemplary_trainY.p','rb'))
        self.m = dtw.KnnDtw()
        self.m.fit(self.training_x, self.training_y)
                
        
    def predict_one(self,testing_pt):
        """
        Arguments
        ----------
            testing_x: a list of points to predict

        Returns
        -------
            a list of predicted letters
        """
        preprocessed = preprocess(testing_pt, self.sample_rate)
        return self.m.predict([preprocessed])[0][0]
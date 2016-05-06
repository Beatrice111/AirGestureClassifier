# -*- coding: utf-8 -*-
"""
Created on Fri May  6 13:28:56 2016

@author: hjsong
"""
import pickle 
import knn_dtw_class as dtw

class Recognizer(object):
    """
    Uses exemplary points from the training data to make predictions on the test data
    """
    def __init__(self):
        self.training_x = pickle.load(open('data/filtered/exemplary_trainX.p','rb'))
        self.training_y = pickle.load(open('data/filtered/exemplary_trainY.p','rb'))
        
    def predict(self,testing_x):
        """
        Arguments
        ----------
            testing_x: a list of points to predict
        
        
        Returns
        -------
            a list of predicted letters
        """
        m = dtw.KnnDtw()
        m.fit(self.training_x, self.training_y)
        predictions = m.predict(testing_x)[0]
        return predictions
  
    def getAccuracy(self, predictions, testing_y):
        num_correct_predictions = 0
        for i in range(len(testing_y)):
        	if predictions[i] == testing_y[i]:
        		num_correct_predictions += 1
        print "number of correct predictions is ", num_correct_predictions
        return num_correct_predictions/float(len(testing_y))

    
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:44:21 2016

@author: hjsong
"""

import numpy as np
import matplotlib.pyplot as plt
import knn_dtw_class as dtw
import pickle
from exemplary_points import getExemplariesExcept
TEST_UID = 1
all_data = pickle.load(open("pickle_data/all_data.p", "rb"))
all_labels = pickle.load(open("pickle_data/all_labels.p", "rb"))

# separate into training data and testing data
training_x, training_y = getExemplariesExcept(TEST_UID)
testing_x = pickle.load(open('data/filtered/user%d/%d_data.p'%(TEST_UID,TEST_UID),'rb'))
testing_y = pickle.load(open('data/filtered/user%d/%d_labels.p'%(TEST_UID,TEST_UID),'rb'))

#test on different k values
accuracies = []

for k in range(1,10):

    m = dtw.KnnDtw(n_neighbors=k)
    m.fit(training_x, training_y)
    predictions = m.predict(testing_x)[0]
    
    num_correct_predictions = 0
    for i in range(len(testing_y)):
    	if predictions[i] == testing_y[i]:
    		num_correct_predictions += 1
    print "number of correct predictions is ", num_correct_predictions
    accuracies.append(num_correct_predictions)

plt.plot(accuracies)
plt.show()
#started: 12:55am
#ended:
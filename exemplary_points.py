# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:26:36 2016

Choose user-dependent exemplary points
    -> n exemplary points per letter per person
    -> Total 10 * n exemplary points per person
    
@author: hjsong
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle
import knn_dtw_class as dtw
import time
from preprocess import preprocess

def filter_and_getExemplaries(all_data, sample_rate, num_per_letter_per_person = 1):
    exemplary_data = []
    exemplary_labels = []

    for D in all_data:
        for letter_idx in range(1,11):
            user_data = D[10*(letter_idx-1):10*letter_idx]
            letter_data = []
            letter_labels = []
            for label, data in user_data:          
                letter_labels.append(label)
                d = np.array(data)
                letter_data.append(preprocess(d[:, 7:9], sample_rate))
            label = letter_labels[0]
            n = len(letter_data)
            
            s = time.time()
            m = dtw.KnnDtw()
            dmtx = np.zeros((n,n))
            for i in range(n-1):
                for j in range(i+1, n):
                    d = m._dtw_distance(letter_data[i], letter_data[j])
                    dmtx[i][j] = d
                    dmtx[j][i] = d
            e = time.time()
            
            # remove outliers
            dsums = dmtx.sum(axis=0)
            mean = dsums.mean()
            std = dsums.std()
            outliers = []
            for i in range(n):
                if (dsums[i] < mean-2*std or mean+2*std < dsums[i]):
                    outliers.append(i)
            for outlier in outliers:
                for i in range(n):
                    dmtx[i][outlier] = 0

            # choose exemplary points
            dsums = dmtx.sum(axis=0)
            arg_mins = np.argpartition(dsums, num_per_letter_per_person)[:num_per_letter_per_person]
            for ind in arg_mins:
                exemplary_data.append(letter_data[ind])
                exemplary_labels.append(label)

    pickle.dump(exemplary_data, open("data/exemplary_trainX.p", "wb"))
    pickle.dump(exemplary_labels, open("data/exemplary_trainY.p", "wb"))
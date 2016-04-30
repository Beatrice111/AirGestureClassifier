# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:47:09 2016

@author: hjsong
"""

import numpy as np
import matplotlib.pyplot as plt
import knn_dtw_class as dtw
import pickle
all_data = pickle.load(open("pickle_data/all_data.p", "rb"))
all_labels = pickle.load(open("pickle_data/all_labels.p", "rb"))

for u_idx in range(1,11):
    user_data = all_data[100*(u_idx-1):100*u_idx]
    user_labels = all_labels[100*(u_idx-1):100*u_idx]
    pickle.dump(user_data,open("data/data_noID/user"+ str(u_idx)+"_data.p", "wb"))
    pickle.dump(user_labels,open("data/data_noID/user"+ str(u_idx)+"_labels.p", "wb"))


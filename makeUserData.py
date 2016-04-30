# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:04:27 2016
Combine all letter_data to user_data and letter_labels to user_labels
@author: hjsong
"""
import os, sys
import pickle
letters = ['O' ,'I', 'J', 'L', 'Z', 'S', 'V', 'T', 'X', 'B']

#u_idx = 1
all_filtered_data = []
all_filtered_labels = []
for u_idx in range(1,11):
    user_data = []
    user_labels = []
    
    for letter in letters:
        data_fpath = 'data/filtered/dump/%d_%s_data.p'%(u_idx, letter)
        label_fpath = 'data/filtered/dump/%d_%s_labels.p'%(u_idx, letter)
    
        letter_data = pickle.load(open(data_fpath, "rb"))
        letter_labels = pickle.load(open(label_fpath, "rb"))
        user_data += letter_data
        user_labels += letter_labels
    all_filtered_data += user_data
    all_filtered_labels += user_labels
    
    #write out inidividual user's data
    d_outpath = 'data/filtered/user%d/%d_data.p'%(u_idx,u_idx)
    l_outpath = 'data/filtered/user%d/%d_labels.p'%(u_idx,u_idx)
    pickle.dump(user_data, open(d_outpath, "wb"))
    pickle.dump(user_labels, open(l_outpath, "wb"))

#write out all_filtered_data of all users
pickle.dump(all_filtered_data, open('data/filtered/all_filtered_data.p','wb'))
pickle.dump(all_filtered_labels, open('data/filtered/all_filtered_labels.p','wb'))

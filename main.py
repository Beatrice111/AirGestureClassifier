import numpy as np
import knn_dtw_class as dtw

N_users = 10

# load all the data
for i in range(N_users):
	execfile("data/user" + str(i + 1) + ".py")

# preprocessing
all_data = []
all_labels = []
for D in [data_user1, data_user2, data_user3, data_user4, data_user5, \
	data_user6, data_user7, data_user8, data_user9, data_user10]:
	for label, d in D:
		d = np.array(d)
		# only extract ax, ay out of the signals
		d = d[:, 7:9]
		# scale the data to be in range [-1,1]
		d = d / np.amax(np.abs(d), axis = 0)
		all_data.append(d)
		all_labels.append(label)

# separate into training data and testing data
training_x = all_data[:900]
training_y = all_labels[:900]
testing_x = all_data[900:]
testing_y = all_labels[900:]

m = dtw.KnnDtw()
m.fit(training_x, training_y)
print m.predict(testing_x)


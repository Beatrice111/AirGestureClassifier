import numpy as np
import knn_dtw_class as dtw

N_users = 10

# load all the data
for i in range(N_users):
	execfile("data/user" + str(i + 1) + ".py")

# preprocessing
sample_rate = 10
all_data = []
all_labels = []
for D in [data_user1, data_user2, data_user3, data_user4, data_user5, \
	data_user6, data_user7, data_user8, data_user9, data_user10]:
	for label, d in D:

		d = np.array(d)
		# TODO: make this a function
		# only extract ax, ay out of the signals
		d = d[:, 7:9]

		# average sample every sample_rate letters
		l, _ = d.shape
		if l < sample_rate:
			d = np.mean(d, axis = 0).reshape(-1, 2)
		else:
			new_l = (l / sample_rate) * sample_rate
			remaining_d = d[new_l:, :]
			d = d[:new_l, :]
			d = np.mean(d.reshape(-1,sample_rate,2), axis = 1)
			if new_l != l:
				d = np.vstack((d, np.mean(remaining_d, axis = 0)))

		# scale the data to be in range [-1,1]
		d = d / np.amax(np.abs(d), axis = 0)
		all_data.append(d)
		all_labels.append(label)

# separate into training data and testing data
# training_x = all_data[:900]
# training_y = all_labels[:900]
# testing_x = all_data[900:]
# testing_y = all_labels[900:]

m = dtw.KnnDtw()
m.fit(training_x, training_y)
predictions = m.predict(testing_x)[0]

num_correct_predictions = 0
for i in range(len(testing_y)):
	if predictions[i] == testing_y[i]:
		num_correct_predictions += 1
print "number of correct predictions is ", num_correct_predictions
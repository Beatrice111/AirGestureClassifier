import numpy as np

def preprocess(d, sample_rate):
	d = np.array(d)
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
	return d
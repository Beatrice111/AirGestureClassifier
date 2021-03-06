import numpy as np
from Recognizer import Recognizer
from exemplary_points import filter_and_getExemplaries

sample_rate = 10

# load data
N_users = 10
for i in range(N_users):
    execfile("data/user" + str(i + 1) + ".py")
all_data = [data_user1, data_user2, data_user3, data_user4, data_user5, \
        data_user6, data_user7, data_user8, data_user9, data_user10]

# extract exemplary points
filter_and_getExemplaries(all_data, sample_rate)

# make prediction
recognizer = Recognizer(sample_rate)
# The data is from letter "O"
print recognizer.predict_one([[ 0.00151,  0.01135],
       [ 0.01175,  0.02839], 
       [ 0.0243 , -0.00781],
       [ 0.01606, -0.03011],
       [-0.01251, -0.02651],
       [-0.08557,  0.02435],
       [-0.05574,  0.02611],
       [ 0.00386,  0.01013],
       [ 0.03279,  0.00049],
       [ 0.02381, -0.0027 ],
       [-0.0126 , -0.00321],
       [-0.06615,  0.01246],
       [-0.06997,  0.00418],
       [-0.06926, -0.00977],
       [-0.0444 , -0.01925],
       [ 0.00515, -0.02594],
       [ 0.01419, -0.02939],
       [ 0.00689, -0.01478],
       [ 0.00534, -0.01004],
       [-0.00194, -0.01154],
       [-0.01755, -0.0048 ],
       [-0.0367 , -0.0101 ],
       [-0.05585,  0.00492],
       [-0.03075,  0.01247],
       [ 0.01603, -0.02082],
       [ 0.04772, -0.01042],
       [ 0.05997, -0.0237 ],
       [ 0.06643, -0.01772],
       [ 0.06918, -0.03335],
       [ 0.03628, -0.02608],
       [ 0.00226, -0.02846],
       [-0.02239, -0.0335 ],
       [-0.01809, -0.02101],
       [ 0.00458, -0.02708],
       [ 0.04297, -0.01898],
       [ 0.04428, -0.02196],
       [ 0.0461 , -0.01883],
       [ 0.04764, -0.01617],
       [ 0.04353, -0.01103],
       [ 0.02812, -0.00314],
       [ 0.03248,  0.00109],
       [ 0.03762,  0.00695],
       [ 0.04361,  0.03073],
       [ 0.08283,  0.0351 ],
       [ 0.10309,  0.03729],
       [ 0.10967,  0.03234],
       [ 0.09297,  0.03389],
       [ 0.07682,  0.03755],
       [ 0.06279,  0.03126],
       [ 0.05293,  0.04366],
       [ 0.06875,  0.02977],
       [ 0.09882,  0.01598],
       [ 0.10159,  0.033  ],
       [ 0.07515,  0.04218],
       [ 0.06301,  0.05765],
       [ 0.08425,  0.06191],
       [ 0.09699,  0.06759],
       [ 0.1206 ,  0.07653],
       [ 0.13856,  0.06708],
       [ 0.12165,  0.05565],
       [ 0.08143,  0.04891],
       [ 0.03951,  0.0491 ],
       [ 0.01667,  0.06773],
       [ 0.05021,  0.06677],
       [ 0.07026,  0.07731],
       [ 0.07586,  0.08146],
       [ 0.04864,  0.10075],
       [ 0.03844,  0.11754],
       [ 0.04003,  0.13108],
       [ 0.03609,  0.13441],
       [ 0.04085,  0.14212],
       [ 0.05166,  0.14062],
       [ 0.06583,  0.12426],
       [ 0.0492 ,  0.12101],
       [ 0.0007 ,  0.12551],
       [-0.0588 ,  0.15164],
       [-0.08867,  0.18127],
       [-0.09355,  0.17274],
       [-0.06339,  0.16674],
       [-0.01699,  0.13315],
       [-0.00826,  0.11014],
       [-0.05615,  0.11281],
       [-0.08851,  0.12137],
       [-0.11803,  0.09253],
       [-0.18607,  0.07499],
       [-0.27438,  0.08757],
       [-0.29094,  0.0888 ],
       [-0.27781,  0.10113],
       [-0.24391,  0.12055],
       [-0.19138,  0.11726],
       [-0.05853,  0.06355],
       [-0.06276,  0.06757],
       [-0.09657,  0.08044],
       [-0.15041,  0.11714],
       [-0.17842,  0.11232],
       [-0.15867,  0.1157 ],
       [-0.10131,  0.08026],
       [-0.04433,  0.06854],
       [-0.03394,  0.06999],
       [-0.10612,  0.0752 ],
       [-0.16917,  0.07614],
       [-0.19824,  0.05859],
       [-0.23906,  0.02559],
       [-0.28237,  0.01072],
       [-0.275  ,  0.00742],
       [-0.24028,  0.00379],
       [-0.21329,  0.011  ],
       [-0.19862,  0.02178],
       [-0.17131, -0.00621],
       [-0.22919, -0.00324],
       [-0.22477, -0.01814],
       [-0.23351, -0.01858],
       [-0.24157, -0.02224],
       [-0.22574, -0.04861],
       [-0.19903, -0.05846],
       [-0.19091, -0.0513 ],
       [-0.20326, -0.04023],
       [-0.23664, -0.015  ],
       [-0.29345,  0.05781],
       [-0.31458,  0.07667],
       [-0.26442,  0.04961],
       [-0.17677, -0.00588],
       [-0.08449, -0.03788],
       [-0.01892, -0.08541],
       [-0.00373, -0.09246],
       [-0.03936, -0.07114],
       [-0.11642, -0.05935],
       [-0.27019, -0.0206 ],
       [-0.29504, -0.02819],
       [-0.28843, -0.04175],
       [-0.25511, -0.06922],
       [-0.21451, -0.09433],
       [-0.18227, -0.107  ],
       [-0.17173, -0.12412],
       [-0.15327, -0.14003],
       [-0.15713, -0.12242],
       [-0.16292, -0.11192],
       [-0.16354, -0.11108],
       [-0.13985, -0.10706],
       [-0.09702, -0.13588],
       [-0.05712, -0.1646 ],
       [-0.04146, -0.17005],
       [-0.0363 , -0.17174],
       [-0.03181, -0.18478],
       [-0.02413, -0.16934],
       [ 0.01779, -0.17253],
       [ 0.07116, -0.1772 ],
       [ 0.08465, -0.18195],
       [ 0.07581, -0.17961],
       [ 0.05687, -0.17762],
       [ 0.0479 , -0.17445],
       [ 0.05553, -0.1695 ],
       [ 0.0812 , -0.16623],
       [ 0.06996, -0.15617],
       [ 0.07813, -0.14337],
       [ 0.14381, -0.13959],
       [ 0.16074, -0.13649],
       [ 0.13749, -0.13316],
       [ 0.09685, -0.10992],
       [ 0.07748, -0.10592],
       [ 0.04463, -0.10235],
       [ 0.01953, -0.08295],
       [ 0.05323, -0.08252],
       [ 0.11325, -0.07792],
       [ 0.15248, -0.08683],
       [ 0.16302, -0.07415],
       [ 0.15371, -0.06336],
       [ 0.14426, -0.04136],
       [ 0.16338, -0.03648],
       [ 0.16655, -0.01855],
       [ 0.16857, -0.00668],
       [ 0.16588,  0.00957],
       [ 0.12747,  0.00928],
       [ 0.05443,  0.02958],
       [ 0.07302,  0.01578],
       [ 0.13824,  0.00978],
       [ 0.16932,  0.01838],
       [ 0.18614,  0.01675],
       [ 0.18945,  0.0333 ],
       [ 0.1759 ,  0.03914],
       [ 0.12662,  0.05002],
       [ 0.06365,  0.0669 ],
       [ 0.02928,  0.0889 ],
       [ 0.03973,  0.09537],
       [ 0.10827,  0.08511],
       [ 0.15349,  0.07932],
       [ 0.13977,  0.08395],
       [ 0.11903,  0.09794],
       [ 0.11878,  0.10763],
       [ 0.11413,  0.10545],
       [ 0.09788,  0.11703],
       [ 0.08087,  0.11789],
       [ 0.06235,  0.10849],
       [ 0.02345,  0.09448],
       [-0.01339,  0.07788],
       [-0.04899,  0.07986],
       [-0.02243,  0.09407],
       [ 0.06814,  0.07168],
       [ 0.14048,  0.08334],
       [ 0.19386,  0.07119],
       [ 0.20143,  0.06   ],
       [ 0.15021,  0.07154],
       [ 0.06284,  0.09412],
       [ 0.05682,  0.09874],
       [ 0.07711,  0.09104],
       [ 0.12498,  0.06361],
       [ 0.14163,  0.04475],
       [ 0.14446,  0.04278],
       [ 0.15864,  0.02672],
       [ 0.11404,  0.02865],
       [ 0.04716,  0.05785],
       [-0.09326,  0.06571],
       [-0.12736,  0.07334],
       [-0.13784,  0.05695],
       [-0.12645,  0.03744],
       [-0.09848,  0.02834],
       [-0.05796,  0.01658],
       [-0.00967,  0.01503],
       [ 0.01194,  0.018  ],
       [-0.01055,  0.02004],
       [-0.08592,  0.03071],
       [-0.3283 ,  0.0856 ],
       [-0.33809,  0.08537],
       [-0.28508,  0.07754],
       [-0.19626,  0.05166],
       [-0.1481 ,  0.04386],
       [-0.11002,  0.04826],
       [-0.09196,  0.04796],
       [-0.10708,  0.05731],
       [-0.12192,  0.06789],
       [-0.16984,  0.07757],
       [-0.14871,  0.07775],
       [-0.11929,  0.07234],
       [-0.09506,  0.06398],
       [-0.09172,  0.06462],
       [-0.11448,  0.06308],
       [-0.12922,  0.07414]])
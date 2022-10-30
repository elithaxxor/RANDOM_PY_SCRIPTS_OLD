import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.cluster import hierarchy
from scipy.spatial import distance_matrix
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_blobs


'''
%matplotlib inline
AGGLORMATIVE CLUSTERING- 
ALL obverations fall on one cluster and pairs of clusteres are split as they move up heirachy 
More popular? 
'''


'''
1. Create random dataset with make_blobs 
2. Plot scatterplot 
## start clustering random datapoints 
3. save the results 
4. fit the model 
5. display results 

'''

#1
X1, y1 = make_blobs(n_samples=50, centers=[[4,4], [-2, -1], [1, 1], [10,4]], cluster_std=0.9)
#2
plt.scatter(X1[:, 0], X1[:, 1], marker='o')

###
#3.
agglom = AgglomerativeClustering(n_clusters = 4, linkage = 'average')
#4.
agglom.fit(X1,y1)
#5.
plt.figure(figsize=(6, 4))
# Create a minimum and maximum range of X1.
x_min, x_max = np.min(X1, axis=0), np.max(X1, axis=0)

# Get the average distance for X1.
X1 = (X1 - x_min) / (x_max - x_min)

# This loop displays all of the datapoints.
for i in range(X1.shape[0]):
    # Replace the data points with their respective cluster value
    # (ex. 0) and is color coded with a colormap (plt.cm.spectral)
    plt.text(X1[i, 0], X1[i, 1], str(y1[i]),
             color=plt.cm.nipy_spectral(agglom.labels_[i] / 10.),
             fontdict={'weight': 'bold', 'size': 9})

# Remove the x ticks, y ticks, x and y axis
plt.xticks([])
plt.yticks([])
# plt.axis('off')

# Display the plot of the original data before clustering
plt.scatter(X1[:, 0], X1[:, 1], marker='.')
plt.show()






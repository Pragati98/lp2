#Importing Packages

import numpy as np  
import pandas as pd  


#Read Dataset
dataset=pd.read_csv("knn_data.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,2].values

# import KNeighborsClassifier and create object of it
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)

#predict class for the points(6,6)
X_test=np.array([6,6])
print X_test
y_pred = classifier.predict([X_test])
print 'General KNN: ',y_pred

# Evaluating the Algorithm  
classifier=KNeighborsClassifier(n_neighbors=3, weights='distance')


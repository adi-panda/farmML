import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
    

crop = pd.read_csv('./cropdata.csv')
crop = crop.sort_values('label')

x = crop.drop(['label'], axis = 1)
y = crop['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20,shuffle = True, random_state = 0)

kn_classifier = KNeighborsClassifier()
kn_classifier.fit(X_train,y_train)

pred_kn = kn_classifier.predict(X_test)

print('Training set score: {:.4f}'.format(kn_classifier.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(kn_classifier.score(X_test, y_test)))


import pickle 

# Its important to use binary mode 
knnPickle = open('knnpickle_file', 'wb') 
      
# source, destination 
pickle.dump(kn_classifier, knnPickle)  

# close the file
knnPickle.close()

print("done")
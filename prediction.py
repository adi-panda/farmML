import pickle
import numpy as np
import array
from sklearn.neighbors import KNeighborsClassifier

loaded_model = pickle.load(open('knnpickle_file', 'rb'))

def prediction(x):
 print(str(loaded_model.predict(x)[0]))
 return str(loaded_model.predict(x)[0])

# N = input('What is N?')
# P = input('What is P?')
# K = input('What is K?')
# temperature = input('What is temp?')
# humidity = input('What is humidity?')
# pH = input('What is pH?')
# rainfall = input('What is rainfall?')

def getUser(answer):
    answer = answer.split(", ")
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    arr = np.array([answer])
    print(arr)
    return prediction(arr)
    #x = [N, P, K, temperature, humidity, pH, rainfall]

#x = [N, P, K, temperature, humidity, pH, rainfall]
#x = np.array(x, dtype=float)

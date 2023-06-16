import pickle
import sys
from sklearn.datasets import load_iris


file_path = str(sys.argv[1])

iris = load_iris()
X = iris.data
y = iris.target

with open(file_path, 'rb') as f:
    lr = pickle.load(f)

prediction = lr.predict([X[0]])

print(prediction)

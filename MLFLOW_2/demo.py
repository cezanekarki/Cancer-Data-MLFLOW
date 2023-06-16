import sys
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

lr = LogisticRegression()
lr.fit(X_train,y_train)

with open('model.pkl','wb') as f:
    pickle.dump(lr,f)

print('Model trained and saved')

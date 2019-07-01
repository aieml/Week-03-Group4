import pickle

train_data=pickle.load(open('train_data.pickle','rb'))
train_target=pickle.load(open('train_target.pickle','rb'))

from sklearn.neighbors import KNeighborsClassifier

clsfr=KNeighborsClassifier()
clsfr.fit(train_data,train_target)

from sklearn.externals import joblib

joblib.dump(clsfr,'KNN_Model.sav')

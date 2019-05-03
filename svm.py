import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

y = np.array(np.load('label.npy').tolist())
X = np.array(np.load('feat.npy').tolist())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=233)

# Simple SVM
clf = SVC(C=20.0, gamma=0.00001)
start = time.time()
clf.fit(X_train, y_train)
acc = clf.score(X_test, y_test)

print('Test accuracy:', acc)
print('Training took: %d seconds' % int(time.time() - start))
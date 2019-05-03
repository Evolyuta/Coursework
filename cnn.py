from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import time
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from sklearn.model_selection import train_test_split

y = np.array(np.load('label.npy').tolist())
X = np.array(np.load('feat.npy').tolist())
lb = LabelEncoder()
yy = np_utils.to_categorical(lb.fit_transform(y))


class_count = yy.shape[1]

# Build the Neural Network
model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(40, 1)))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(128, 3, activation='relu'))
model.add(Conv1D(128, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(class_count, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.4, random_state=233)

X_train = np.expand_dims(X_train, axis=2)
X_test = np.expand_dims(X_test, axis=2)

start = time.time()
model.fit(X_train, y_train,  batch_size=32, epochs=50)
score, acc = model.evaluate(X_test, y_test, batch_size=16)
#
# print('Test score:', score)
print('Test accuracy:', acc)
print('Training took: %d seconds' % int(time.time() - start))
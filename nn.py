from sklearn.preprocessing import LabelEncoder
import numpy as np
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
import time

Y = np.array(np.load('label.npy').tolist())
X = np.array(np.load('feat.npy').tolist())
lb = LabelEncoder()
yy = np_utils.to_categorical(lb.fit_transform(Y))

num_labels = yy.shape[1]
filter_size = 2

# build model
model = Sequential()

model.add(Dense(256, input_shape=(40,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(num_labels))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

aTrain, aTest, bTrain, bTest = train_test_split(X, yy, test_size=0.4, random_state=233)


start = time.time()
model.fit(aTrain, bTrain, batch_size=32, epochs=50, validation_data=(aTest, bTest))
score, acc = model.evaluate(aTest, bTest, batch_size=16)
#
# print('Test score:', score)
print('Test accuracy:', acc)
print('Training took: %d seconds' % int(time.time() - start))

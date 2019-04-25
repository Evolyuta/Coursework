import librosa
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import numpy as np
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
import os
import time

start = time.time()
import sys
import tensorflow as tf

tf.logging.info('TensorFlow')
# INFO:tensorflow:TensorFlow
tf.logging.set_verbosity(tf.logging.ERROR)
tf.logging.info('TensorFlow')

# train=pd.read_csv('dataset/Urban/train.csv')
train = pd.read_csv('Music/train.csv')
train.head()


def parser_label(row):
    print(row.ID)
    label = row.Class
    return label


def parser_feature(row):
    print(row.ID)
    try:
        # filename='dataset/Urban/Train/'+str(row.ID)+'.wav'
        filename = 'Music/' + str(row.ID) + '.wav'
        X, sample_rate = librosa.load(filename, res_type='kaiser_fast')
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        return mfccs
    except Exception as e:
        print('Error in ', filename)
        return None, None
    feature = mfccs
    return feature


s = 0
m = 0

time_start = time.time()
seconds = 0
minutes = 0

# temp=train.apply(parser,axis=1)
# temp.columns=['feature','label']
temp_label = train.apply(parser_label, axis=1)
temp_feature = train.apply(parser_feature, axis=1)

Y = np.array(temp_label.tolist())
X = np.array(temp_feature.tolist())
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

aTrain, aTest, bTrain, bTest = train_test_split(X, yy, test_size=0)
model.fit(aTrain, bTrain, batch_size=32, epochs=500, validation_data=(aTest, bTest))

end = time.time()
print(end - start)

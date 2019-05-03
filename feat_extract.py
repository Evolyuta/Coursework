import librosa
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import time
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from sklearn.model_selection import train_test_split
import tensorflow as tf

tf.logging.info('TensorFlow')
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

np.save('feat.npy', temp_feature)
np.save('label.npy', temp_label)
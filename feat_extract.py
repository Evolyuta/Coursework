import librosa
import pandas as pd
import time
import numpy as np
import tensorflow as tf

tf.logging.info('TensorFlow')
tf.logging.set_verbosity(tf.logging.ERROR)
tf.logging.info('TensorFlow')

train = pd.read_csv('Music/train.csv')
train.head()


def parser_label(row):
    print(row.ID)
    label = row.Class
    return label


def parser_feature(row):
    print(row.ID)
    try:
        filename = 'Music/' + str(row.ID) + '.mp3'
        X, sample_rate = librosa.load(filename, res_type='kaiser_fast')
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        return mfccs
    except Exception as e:
        print('Error in ', filename)
        return None, None
    feature = mfccs
    return feature


start = time.time()

temp_label = train.apply(parser_label, axis=1)
temp_feature = train.apply(parser_feature, axis=1)

np.save('feat.npy', temp_feature)
np.save('label.npy', temp_label)
print('Extracting took: %d seconds' % int(time.time() - start))
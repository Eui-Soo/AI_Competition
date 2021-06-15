import tensorflow as tf
from tensorflow import keras


def model_train(framework='tensorflow',model_name='DEC_v1'):
    if framework == 'tensorflow':
        tmp=1
    elif framework =='pytorch':
        tmp=1
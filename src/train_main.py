import os
os.environ['TF_DETERMINISTIC_OPS'] = '1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from models_train import model_train
from data_load import dataloader
import pandas as pd

def main():
    
    train_X=dataloader()

    model=model_train()

    


if __name__ == '__main__':
    framework='tensorflow'
    model_name='DEC_v1'
    data_mode=0

    main()
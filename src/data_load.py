import pandas as pd
import numpy as np
import os

def data_loader():
    list_csv = os.listdir('../data/')
    list_csv=sorted(list_csv)

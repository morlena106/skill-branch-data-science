import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from copy import deepcopy
from tqdm import tqdm

from sklearn.datasets import make_regression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
%matplotlib inline

def split_data_into_two_samples(data):
    
    train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    
    return train_data, test_data


def prepare_data(data):
    #select_data = data.select_dtypes(exclude=[object])
    data = data.drop(columns=["Id"])
    y = data["SalePrice"]
    data = data.drop(columns=["SalePrice"])
    select_data = data.select_dtypes([np.number])
    return select_data.dropna(axis=1), y

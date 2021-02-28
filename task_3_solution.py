import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.datasets import make_regression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split

def split_data_into_two_samples(data):
    
    train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    
    return train_data, test_data


def prepare_data(data):
    #select_data = data.select_dtypes(exclude=[object])
    data = data.drop(columns=["id"])
    y = data["price_doc"]
    data = data.drop(columns=["price_doc"])
    select_data = data.select_dtypes([np.number])
    return select_data.dropna(axis=1), y

def scale_data(data, scaler):
    numeric_data = data.select_dtypes([np.number])
    numeric_features = numeric_data.columns
    data_scaler = scaler.fit_transform(data[numeric_features])
    return data_scaler

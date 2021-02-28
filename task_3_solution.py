import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.datasets import make_regression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split

#1
def split_data_into_two_samples(data):
    
    train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    
    return train_data, test_data

#2
def prepare_data(data):
    #select_data = data.select_dtypes(exclude=[object])
    data = data.drop(columns=["id"])
    y = data["price_doc"]
    data = data.drop(columns=["price_doc"])
    select_data = data.select_dtypes([np.number])
    return select_data.dropna(axis=1), y

#3
def scale_data(data, scaler):
    numeric_data = data.select_dtypes([np.number])
    numeric_features = numeric_data.columns
    data_scaler = scaler.fit_transform(data[numeric_features])
    return data_scaler

#4
def prepare_data_for_model(data,scaler):
    
    data = data.drop(columns=["id"])
    y = data["price_doc"]
    data = data.drop(columns=["price_doc"])
    
    numeric_data = data.select_dtypes([np.number])
    
    numeric_data = numeric_data.dropna(axis=1)
    
    numeric_features = numeric_data.columns
    
    data_scaler = scaler.fit_transform(numeric_data[numeric_features])
    
    return data_scaler, y 


from sklearn.linear_model import LinearRegression
#5
def fit_first_linear_model(x_train,y_train):
    model = LinearRegression()
    my_model = model.fit(x_train, y_train)
    return my_model

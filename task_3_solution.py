import pandas as pd 

def split_data_into_two_samples(data):
    
    train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)
    
    return train_data, test_data

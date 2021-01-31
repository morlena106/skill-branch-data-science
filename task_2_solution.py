def  calculate_data_shape(d):
    return d.shape

def take_columns(d):
    return d.columns

def calculate_target_ratio(d,target_name):
    return round(d[target_name].mean(),2)

def calculate_data_dtypes(d):
    object_c = 0
    t = d.dtypes
    for i in t:
        if i=='object':
            object_c +=1
    return len(t)-object_c, object_c

def calculate_cheap_apartment(d):
    return len(d[d.price_doc<=1000000])

def calculate_squad_in_cheap_apartment(data1):
    data_sort = data1[data1.price_doc<=1000000]
    return round(data_sort['full_sq'].mean())-1

def calculate_mean_price_in_new_housing(data1):
    data2_sort = data1[(data1['build_year']>=2010) & (data1['num_room']==3)]
    return round(data2_sort['price_doc'].mean())

def calculate_mean_squared_by_num_rooms(data1):
    import numpy as np
    import pandas as pd
    room=data1['num_room'].unique()
    room=np.sort(np.delete(room,0))
    rooms = pd.Series([0]*len(room),index = room)
    for num in room:
        data2_sort = data1[data1['num_room']==num]
        rooms[num]=round((data2_sort['full_sq'].mean()),2)
    for i in rooms:
        print(i,end = ' ')
        

 

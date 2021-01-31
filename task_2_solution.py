import numpy as np
import pandas as pd

#1
def  calculate_data_shape(d):
    return d.shape

#2
def take_columns(d):
    return d.columns

#3
def calculate_target_ratio(d,target_name):
    return round(d[target_name].mean(),2)

#4
def calculate_data_dtypes(d):
    object_c = 0
    t = d.dtypes
    for i in t:
        if i=='object':
            object_c +=1
    return len(t)-object_c, object_c

#5
def calculate_cheap_apartment(d):
    return len(d[d.price_doc<=1000000])

#6
def calculate_squad_in_cheap_apartment(data1):
    data_sort = data1[(data1.price_doc<=1000000) & (data1.price_doc>0) ]
    return round(data_sort['full_sq'].mean())

#7
def calculate_mean_price_in_new_housing(data1):
    data2_sort = data1[(data1['build_year']>=2010) & (data1['num_room']==3)]
    return round(data2_sort['price_doc'].mean())

#8_test
def calculate_mean_squared_by_num_rooms_test(data1):
    
    room=data1['num_room'].unique()
    room=np.sort(np.delete(room,0))
    rooms = pd.Series([0]*len(room),index = room)
    for num in room:
        data2_sort = data1[data1['num_room']==num]
        rooms[num]=round((data2_sort['full_sq'].mean()),2)
    for i in rooms:
        print(i,end = ' ')
        
#8
def calculate_mean_squared_by_num_rooms(data1):
    data2 = data1.groupby('num_room')['full_sq'].mean()
    return round(data2,2)
 
    
#9
def calculate_squared_stats_by_material(data1):
    #material_max = data1.groupby('material')['full_sq'].max()
    #material_min = data1.groupby('material')['full_sq'].min()
    #return round(material_max,2), round(material_min,2)
    return data1.pivot_table('full_sq', index = 'material',aggfunc=['max','min'])

#10
def calculate_crosstab(data1):
    return round(data1.groupby(['sub_area','product_type'])['full_sq'].mean(),2)

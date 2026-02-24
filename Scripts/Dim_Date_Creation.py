import pandas as pd
import numpy as np

def date_dataframe(df, column_name,description):
    dim_df = df[[column_name]].drop_duplicates().copy()
    dim_df = dim_df.rename(columns={column_name: 'date_time'})
    dim_df.insert(0, description + '_id', range(1, len(dim_df)+1))    
    dim_df['day'] = dim_df['date_time'].dt.day
    dim_df['hour'] = dim_df['date_time'].dt.hour
    dim_df['month'] = dim_df['date_time'].dt.month
    dim_df['year'] = dim_df['date_time'].dt.year
    dim_df['weekday'] = dim_df['date_time'].dt.weekday
    conditions = [
        dim_df['weekday'] <= 4,
        dim_df['weekday'] > 4
    ]
    choices = [False, True]
    dim_df['is_weekend'] = np.select(conditions, choices, default='Unknown')
    dim_df['weekday'] = dim_df['weekday'].map({
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thrusday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    })
    return dim_df
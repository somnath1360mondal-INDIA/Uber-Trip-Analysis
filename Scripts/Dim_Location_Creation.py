import pandas as pd

def location_dataframe(df, column_one, column_two, description):
    dim_df = df[[column_one,column_two]].drop_duplicates().copy()
    dim_df.insert(0,description + '_key',range(1,len(dim_df)+1))
    return dim_df
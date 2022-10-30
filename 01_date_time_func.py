# convert time to datetime format
import pandas as pd
import numpy as np

# this is used to locate 2 seperate date iterations and append them to a list using
# date time formate
# df.shape[0] for ro, df.shape[1] for column



def combine_date(df,tab_name)
    list_tab = []
    for i in range(df.shape[0]):
        list_tab.append(df.loc[i, 'Tangal'] + 'T' + df.loc[i, tab_name][0:2])
    return np.array(list_tab, dtype='datetime64')


df['DateTime'] = combine_date(df, 'Jam')


#

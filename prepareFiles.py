import pandas as pd
import numpy as np
 
def deleteTooFar(data, lat, lon):
    w_lat = 111
    w_lon = 64.8
    df = pd.DataFrame(columns=['lat', 'lon', 'type', 'title', 'abs'])
    for i in data:
        i.data['abs']= np.sqrt((((i.data['lon'] - lon) * w_lon) ** 2 ) + ((i.data['lat'] - lat) * w_lat) ** 2)
        i.data = i.data.sort_values(by=['abs'])
        i.data = i.data[0:1]
        df = pd.merge(df, i.data, how='outer')
        df['near'] = np.where(df['abs'] < 2, True, False)
    return df
 
from prepareFiles import deleteTooFar
from ClassGetFiles import getData
 
import pandas as pd
import numpy as np
 
data = getData()
p1 = [54.3620161548644, 18.45468599827991]
p2 = [54.29824016860428, 18.643935370279067]
p3 = [54.35592946122077, 18.75392120660325]
p4 = [54.42783797514661, 18.5486962382665]
x, y = np.meshgrid(np.linspace(p1[0], p3[0], 10), np.linspace(p1[1], p4[1], 10))
# połącz współrzędne x i y, tworząc tablicę zawierającą pary (x, y)
points = np.stack((x, y), axis=-1)
# spłaszcz tablicę punktów
points = points.reshape(-1, 2)
xd = pd.DataFrame(columns=['lat', 'lon', 'wynik'])
 
def returnPercent(lat, lon):
    global xd
    df = deleteTooFar(data, lat, lon)
    title_list = df.loc[df['near'] == True, 'type'].tolist()
    unique_list = list(set(title_list))
    wynik=(len(unique_list)/69*100)
    new_row = pd.DataFrame({'lat': lat, 'lon': lon, 'wynik': wynik}, index=[len(xd)])
    xd = pd.concat([xd, new_row], axis=0)
    return xd
 
def getHeatMap():
    for i in points:
        returnPercent(i[0], i[1])
    return xd
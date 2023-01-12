import requests
import json
import os
import pandas as pd

data_list = []
class CsvFiles():
    
    def __init__(self, path) -> None:
        self.name = self.getName(path)
        self.data = pd.read_csv(path)
        self.lat = self.data['lat']
        self.lon = self.data['lon']
        self.type = self.data['type']

        # self.lat, self.lon, self.type = self.splitData(self.data)
    def getName(self, path):
        return path.split('_')[0].split('/')[1]

    # def splitData(data):
    #     lat = data['lat']
    #     lon = data['lon']
    #     type = data['type']
    #     return lat, lon, type

path = 'data/'
files = []

for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    d = CsvFiles(f)
    data_list.append(d)

length = 0

# for i in data_list:
    # length = length + (len(i.data))
    # print(i.lat,i.lon,i.type)

print(length)

lat_1 = 54.35379183893733
lon_1 = 18.592863067989025
lat_2 = 54.35516237294401	
lon_2 = 18.64964134202087

# call the OSMR API
distances = []
# for i in range(len(data_list[0].type)):
#     lat_2 = data_list[0].lat[i]	
#     lon_2 = data_list[0].lon[i]	
#     r = requests.get(f"http://router.project-osrm.org/route/v1/driving/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")
#     routes = json.loads(r.content)
#     distance = routes.get("routes")[0].get("distance")
#     distances.append(distance)
#     # print(distance)
print(data_list[0].type.shape)
# print(distances)
# print(distances.sort(distances))
# distances.sort(distances)



# then you load the response using the json libray
# by default you get only one alternative so you access 0-th element of the `routes`
# routes = json.loads(r.content)
# print(routes)
# print(routes.get("routes")[0])
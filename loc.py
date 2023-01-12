import requests
import json
import os
import pandas as pd

data_list = []
class CsvFiles():
    def __init__(self, path) -> None:
        self.name = self.getName(path)
        self.data = pd.read_csv(path)

    def getName(self, path):
        return path.split('_')[0].split('/')[1]

path = 'data/'
files = []

for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    d = CsvFiles(f)
    data_list.append(d)

length = 0

for i in data_list:
    print(len(i.data))



# lat_1 = 54.35379183893733
# lon_1 = 18.592863067989025
# lat_2 = 54.35516237294401	
# lon_2 = 18.64964134202087

# # call the OSMR API
# r = requests.get(f"http://router.project-osrm.org/route/v1/driving/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")
# # then you load the response using the json libray
# # by default you get only one alternative so you access 0-th element of the `routes`
# routes = json.loads(r.content)
# print(routes)
# print(routes.get("routes")[0])
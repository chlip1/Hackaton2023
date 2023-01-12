import requests
import json
 
lat_1 = 54.35379183893733
lon_1 = 18.592863067989025
lat_2 = 54.35516237294401	
lon_2 = 18.64964134202087
# call the OSMR API
r = requests.get(f"http://router.project-osrm.org/route/v1/driving/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false""")
# then you load the response using the json libray
# by default you get only one alternative so you access 0-th element of the `routes`
routes = json.loads(r.content)
print(routes)
print(routes.get("routes")[0])
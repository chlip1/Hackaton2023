import pandas as pd

def deleteTooFar(data, loc, lng):
    for i in data:
        print(loc)
        print(i.data)
        i.data = i.data.sort_values(by=['lat'], key=lambda x: abs(i.data['lat']-loc))
        print(i.data)
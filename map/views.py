from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
import pandas as pd
from folium import IFrame
from heatmap import getHeatMap
from folium.plugins import HeatMap
# import geemap.foliumap as geemap
 
#import func from loc.py
from ClassGetFiles import getData
from prepareFiles import deleteTooFar, deleteTooFar_2
# Create your views here.
 
locations = []
 
def index(request):
    return render(request, 'glowna.html')

locations = []

def wybory(request):
 
    data = getData()
 
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/wybory')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
 
    lat = location.lat
    lng = location.lng
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')
 
    data = deleteTooFar(data, lat, lng)
    title_list = data.loc[data['near'] == True, 'type'].tolist()
    bad_list = data.loc[data['near'] == False, 'type'].tolist()
    unique_list = list(set(title_list))
    badd_list = list(set(bad_list))

    wynik=(f"{round((len(unique_list)/69*100),2)}")
    wynik_bad = (badd_list)
 
    x = data["lat"].to_list()
    y = data['lon'].to_list()
    tit= data['type'].to_list()
 
    feature_ea = folium.FeatureGroup(name='Entire home/apt')
    m = folium.Map(location=[54.37 , 18.58], zoom_start=12)
    # print(y)
 
 
    for i in range(0, len(x)):
        popup=data["title"].to_list()
        # żarcie
        if tit[i] == "piekarnia" or tit[i] == "restaurant" or tit[i] == "bar" or tit[i] == "kawiarnia" or tit[i] == "grocery store" or tit[i] == "sklep spozywczy" or tit[i] == "coffee" or tit[i] == "cukiernia" or tit[i] == "fastfood" or tit[i] == "restauracje" or tit[i] == "pub" or tit[i] == "catering":
            clr = 'blue'
        # transport
        elif tit[i] == "serwisrowerowy" or tit[i] == "public transport" or tit[i] == "przystanek" or tit[i] == "Stacje transportu publicznego" or tit[i] == "transport" or tit[i] == "stacjapaliw" or tit[i] == "piekarnia":
            clr = 'red'
        # kultura i nauka
        elif tit[i] == "biblioteka" or tit[i] == "university" or tit[i] == "muzeum" or tit[i] == "school" or tit[i] == "culture" or tit[i] == "przedszkole" or tit[i] == "szkola" or tit[i] == "zlobek":
            clr = 'green'
        # sport i rekraacja
        elif tit[i] == "plaza" or tit[i] == "silownia" or tit[i] == "sport" or tit[i] == "hotel" or tit[i] == "impreza" or tit[i] == "touristattraction" or tit[i] == "plac" or tit[i] == "plac zabaw" or tit[i] == "entertainment"  or tit[i] == "dzieci" or tit[i] == "fitness" or tit[i] == "atrakcje" or tit[i] == "park" or tit[i] == "basen":
            clr = '#FF1493'
        # zawody
        elif tit[i] == "pralnia" or tit[i] == "remonty" or tit[i] == "krawiec" or tit[i] == "sprzatanie" or tit[i] == "drukarnia" or tit[i] == "office" or tit[i] == "stolarz" or tit[i] == "shop" or tit[i] == "mechanik" or tit[i] == "sklepAGD" or tit[i] == "shopping mall" or tit[i] == "monopolowy" or tit[i] == "bank" or tit[i] == "biuro" or tit[i] == "fryzjer" or tit[i] == "prawnik" or tit[i] == "fotograf":
            clr = 'brown'
        # zdrowie
        elif tit[i] == "apteka" or tit[i] == "ortodonta" or tit[i] == "dentysta" or tit[i] == "opiekazdrowotna" or tit[i] == "lekarz" or tit[i] == "przychodnia" or tit[i] == "plac" or tit[i] == "plac zabaw" or tit[i] == "entertainment"  or tit[i] == "dzieci" or tit[i] == "fitness" or tit[i] == "atrakcje" or tit[i] == "park" or tit[i] == "basen":
            clr = '#add8e6'
        # wiara
        elif tit[i] == "cmentarz" or tit[i] == "church" :
            clr = 'black'
        # reszta
        else:
            clr = 'orange'

        folium.CircleMarker(location=(x[i],y[i]),
                        radius=3,
                        tooltip=popup[i],
                        color=clr,
                        fill_color=clr,
                        fill=True).add_to(m)
        folium.Circle(
        location=[lat, lng],
        radius=1300,
        color='#8432e8',
        fill=False,
        fill_color=''
        ).add_to(m)
    lc = folium.map.LayerControl()
    folium.Marker([lat, lng], tooltip='Click for more',
                 ).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
        'wynik': wynik,
        'wynik_bad':wynik_bad,
    }
    return render(request, 'wybory.html', context)
def wybory_rower(request):
 
    data = getData()
 
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/wybory_rower')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
 
    lat = location.lat
    lng = location.lng
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')
 
    data = deleteTooFar_2(data, lat, lng)
    title_list = data.loc[data['near'] == True, 'type'].tolist()
    bad_list = data.loc[data['near'] == False, 'type'].tolist()
    unique_list = list(set(title_list))
    badd_list = list(set(bad_list))

    wynik=(f"{round((len(unique_list)/69*100),2)}")
    wynik_bad = (badd_list)
 
    x = data["lat"].to_list()
    y = data['lon'].to_list()
    tit= data['type'].to_list()
    feature_ea = folium.FeatureGroup(name='Entire home/apt')
    m = folium.Map(location=[54.37 , 18.58], zoom_start=12)
    # print(y)
 
 
    for i in range(0, len(x)):
        popup=data["title"].to_list()
        # żarcie
        if tit[i] == "piekarnia" or tit[i] == "restaurant" or tit[i] == "bar" or tit[i] == "kawiarnia" or tit[i] == "grocery store" or tit[i] == "sklep spozywczy" or tit[i] == "coffee" or tit[i] == "cukiernia" or tit[i] == "fastfood" or tit[i] == "restauracje" or tit[i] == "pub" or tit[i] == "catering":
            clr = 'blue'
        # transport
        elif tit[i] == "serwisrowerowy" or tit[i] == "public transport" or tit[i] == "przystanek" or tit[i] == "Stacje transportu publicznego" or tit[i] == "transport" or tit[i] == "stacjapaliw" or tit[i] == "piekarnia":
            clr = 'red'
        # kultura i nauka
        elif tit[i] == "biblioteka" or tit[i] == "university" or tit[i] == "muzeum" or tit[i] == "school" or tit[i] == "culture" or tit[i] == "przedszkole" or tit[i] == "szkola" or tit[i] == "zlobek":
            clr = 'green'
        # sport i rekraacja
        elif tit[i] == "plaza" or tit[i] == "silownia" or tit[i] == "sport" or tit[i] == "hotel" or tit[i] == "impreza" or tit[i] == "touristattraction" or tit[i] == "plac" or tit[i] == "plac zabaw" or tit[i] == "entertainment"  or tit[i] == "dzieci" or tit[i] == "fitness" or tit[i] == "atrakcje" or tit[i] == "park" or tit[i] == "basen":
            clr = '#FF1493'
        # zawody
        elif tit[i] == "pralnia" or tit[i] == "remonty" or tit[i] == "krawiec" or tit[i] == "sprzatanie" or tit[i] == "drukarnia" or tit[i] == "office" or tit[i] == "stolarz" or tit[i] == "shop" or tit[i] == "mechanik" or tit[i] == "sklepAGD" or tit[i] == "shopping mall" or tit[i] == "monopolowy" or tit[i] == "bank" or tit[i] == "biuro" or tit[i] == "fryzjer" or tit[i] == "prawnik" or tit[i] == "fotograf":
            clr = 'brown'
        # zdrowie
        elif tit[i] == "apteka" or tit[i] == "ortodonta" or tit[i] == "dentysta" or tit[i] == "opiekazdrowotna" or tit[i] == "lekarz" or tit[i] == "przychodnia" or tit[i] == "plac" or tit[i] == "plac zabaw" or tit[i] == "entertainment"  or tit[i] == "dzieci" or tit[i] == "fitness" or tit[i] == "atrakcje" or tit[i] == "park" or tit[i] == "basen":
            clr = '#add8e6'
        # wiara
        elif tit[i] == "cmentarz" or tit[i] == "church" :
            clr = 'black'
        # reszta
        else:
            clr = 'orange'
 
 
 
        folium.CircleMarker(location=(x[i],y[i]),
                        radius=3,
                        tooltip=popup[i],
                        color=clr,
                        fill_color=clr,
                        fill=True).add_to(m)
        folium.Circle(
        location=[lat, lng],
        radius=3000,
        color='#8432e8',
        fill=False,
        fill_color=''
        ).add_to(m)
    lc = folium.map.LayerControl()
    folium.Marker([lat, lng], tooltip='Click for more',
                 ).add_to(m)
 
 
 
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
        'wynik': wynik,
        'wynik_bad':wynik_bad,
    }
    return render(request, 'wybory_rower.html', context)
 
def mapa_kryteria(request):
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    data2 = pd.read_csv("./heat_map.csv")
    x = data2['lat'].to_list()
    y = data2['lon'].to_list()
    wynik = data2['wynik'].to_list()
    heatlist = []
    for i in range(len(x)):
        list = [x[i],y[i],wynik[i]]
        heatlist.append(list)



    # Create Map Object
    m = folium.Map(location=[54.37 , 18.58 ], zoom_start=12)
    wynik1 = []
    for i in range(0,len(x)):
        wynik1 = wynik[i]
        if wynik1 < 25 :
            clr = '#ff0800'
        elif wynik1 >= 25 and wynik1 < 50 :
             clr = '#ff8800'
        elif wynik1 >= 50 and wynik1 < 85 :
             clr = '#fff700'
        elif wynik1 >= 85 and wynik1 < 90 :
             clr = '#80cd23'
        else:
            clr = '#02f502'
        wynik2 = (wynik1)/100

        folium.Circle(location=[x[i], y[i]], radius=500, color="None", fill_color=clr).add_to(m)

    HeatMap(heatlist).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'mapa_kryteria.html', context)

def dostepne(request):
    return render(request, 'dostepne.html')

def zielone(request):
    data2 = pd.read_csv("./heat_map.csv")
    x = data2['lat'].to_list()
    y = data2['lon'].to_list()
    wynik = data2['zielone'].to_list()
    heatlist = []
    for i in range(len(x)):
        list = [x[i],y[i],wynik[i]]
        heatlist.append(list)

    # Create Map Object
    m = folium.Map(location=[54.37 , 18.58 ], zoom_start=12)
    wynik1 = []
    for i in range(0,len(x)):
        wynik1 = wynik[i]
        if wynik1 == False :
            clr = "red"
        else :
            clr = "None"

        folium.Circle(location=[x[i], y[i]], radius=500, color=clr, fill_color=clr).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'zielone.html',context)

def wspolne(request):
    data2 = pd.read_csv("./heat_map.csv")
    x = data2['lat'].to_list()
    y = data2['lon'].to_list()
    wynik = data2['wspolne'].to_list()
    heatlist = []
    for i in range(len(x)):
        list = [x[i],y[i],wynik[i]]
        heatlist.append(list)



    # Create Map Object
    m = folium.Map(location=[54.37 , 18.58 ], zoom_start=12)
    wynik1 = []
    for i in range(0,len(x)):
        wynik1 = wynik[i]
        if wynik1 == False :
            clr = "red"
        else :
            clr = "None"


        folium.Circle(location=[x[i], y[i]], radius=500, color=clr, fill_color=clr).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'wspolne.html',context)

def innowacyjne(request):
    data2 = pd.read_csv("./heat_map.csv")
    x = data2['lat'].to_list()
    y = data2['lon'].to_list()
    wynik = data2['innowacyjne'].to_list()
    heatlist = []
    for i in range(len(x)):
        list = [x[i],y[i],wynik[i]]
        heatlist.append(list)



    # Create Map Object
    m = folium.Map(location=[54.37 , 18.58 ], zoom_start=12)
    wynik1 = []
    for i in range(0,len(x)):
        wynik1 = wynik[i]
        if wynik1 == False :
            clr = "red"
        else :
            clr = "None"


        folium.Circle(location=[x[i], y[i]], radius=500, color=clr, fill_color=clr).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'innowacyjne.html',context)

def dostepne(request):
    data2 = pd.read_csv("./heat_map.csv")
    x = data2['lat'].to_list()
    y = data2['lon'].to_list()
    wynik = data2['dostepne'].to_list()
    heatlist = []
    for i in range(len(x)):
        list = [x[i],y[i],wynik[i]]
        heatlist.append(list)



    # Create Map Object
    m = folium.Map(location=[54.37 , 18.58 ], zoom_start=12)
    wynik1 = []
    for i in range(0,len(x)):
        wynik1 = wynik[i]
        if wynik1 == False :
            clr = "red"
        else :
            clr = "None"


        folium.Circle(location=[x[i], y[i]], radius=500, color=clr, fill_color=clr).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'dostepne.html',context)
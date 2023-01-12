from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
import pandas as pd

# Create your views here.

locations = []

def index(request):
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    data = pd.read_csv("C:\\Users\\bieni\Hackaton2023-main\\average-latitude-longitude-countries.csv")
    latitude = data['Latitude'].tolist()
    longitude = data['Longitude'].tolist()
    print(latitude)
    locations.append([lat,lng])
    print(locations)
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')


    # Create Map Object
    m = folium.Map(location=[55, 18], zoom_start=10)
    #
    # for x in range(0, len(longitude)):
    #     folium.Marker((latitude[x],longitude[x]), icon=folium.DivIcon(html=f"""
    #         <div><svg>
    #             <circle r="10" fill="#69b3a2"/>
    #         </svg></div>""")).add_to(m)
    #
    # folium.Marker([lat, lng], tooltip='Click for more',
    #               popup=country).add_to(m)
    # Get HTML Representation of Map Object
    # m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)
locations = []
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    data = pd.read_csv("C:\\Users\\bieni\Hackaton2023-main\\average-latitude-longitude-countries.csv")
    latitude = data['Latitude'].tolist()
    longitude = data['Longitude'].tolist()
    print(latitude)
    locations.append([lat, lng])
    print(locations)
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[1, 25], zoom_start=1)

    for x in range(0, len(longitude)):
        folium.Marker((latitude[x], longitude[x]), icon=folium.DivIcon(html=f"""
            <div><svg>
                <circle r="10" fill="#69b3a2"/>
            </svg></div>""")).add_to(m)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'search.html', context)

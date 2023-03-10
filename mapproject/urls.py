"""mapproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from map import views as map_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_views.index, name='index'),
    # path('search/', map_views.search, name='search'),
    # path('obszar/', map_views.obszar, name='obszar'),
    path('wybory/', map_views.wybory, name='wybory'),
    path('wybory_rower/', map_views.wybory_rower, name='wybory_rower'),
    path('zielone/', map_views.zielone, name='zielone'),
    path('dostepne/', map_views.dostepne, name='dostepne'),
    path('innowacyjne/', map_views.innowacyjne, name='innowacyjne'),
    path('wspolne/', map_views.wspolne, name='wspolne'),
    path('mapa_kryteria/', map_views.mapa_kryteria, name='mapa_kryteria'),
]
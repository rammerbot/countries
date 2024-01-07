
from django.urls import path, include
from .views import *




urlpatterns = [
    #path('countries/',CountryAPIView.as_view(), name='countries'),
    path('countries/',countries_api_view, name='countries'),
    path('language/',language_api_view, name='language'),
    path('floor/', floor_api_view, name='floor'),
    path('museums/',museum_api_view, name='museums'),
    path('museums/<int:pk>/', detail_museum_api_view, name='museum_detail'),
    path('floor/<int:pk>/',detail_floor_api_view, name='floor_detail'),
    path('countries/<int:pk>', detail_country_api_view, name='counties_detail'),
    path('language/<int:pk>', detail_language_api_view, name='language_detail'),
    path('idiomas/', LanguageApiView.as_view(), name='idiomas'),
    path('country/<int:pk>', CountryUpdateAPIView.as_view(), name='pais'),
    path('museum_detail/<int:pk>', MuseumRetrieveApiView.as_view(), name='museum_detail2'),
     
]

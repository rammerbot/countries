from rest_framework import viewsets

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Countries, Languages, Floor, Museum
from .serializers import CountriesSerializer, LanguageSerializer, FloorSerializer, MuseumSerializer





# Create your views here.

# class CountryAPIView(APIView):
#     def get(self, request):
#         countries = Countries.objects.all()
#         countries_serializer = CountriesSerializer(countries, many=True)
#         return Response(countries_serializer.data)


# Vista de listado de paises y crer paises
class MuseumRetrieveApiView(RetrieveAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer

class CountryUpdateAPIView(UpdateAPIView):
    serializer_class = MuseumSerializer
    queryset = Museum.objects.all()
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class LanguageApiView(ListAPIView):
    serializer_class = MuseumSerializer
    def get_queryset(self):
        return Museum.objects.all()



@api_view(['GET','POST'])
def countries_api_view(request):

    # Consulta de datos
    countries = Countries.objects.all()
    # Validacion de datos
    if countries:
        #Validcion de metodo Get
        if request.method == 'GET':
            countries_serializer = CountriesSerializer(countries, many=True)
            return Response(countries_serializer.data, status= status.HTTP_200_OK)
        #Validacion de metodo Post
        elif request.method == 'POST':
            countries_serializer = CountriesSerializer(data = request.data)
            #validacion de datos en serializador
            if countries_serializer.is_valid():
                countries_serializer.save()
                return Response(countries_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(countries_serializer.errors)
    else:
        return Response({'message':'Bad request'}, status=status.HTTP_400_BAD_REQUEST) 

    
@api_view(['GET','PUT', 'DELETE'])
def detail_country_api_view(request, pk):
    
    #Consulta
    country = Countries.objects.filter(pk=pk).first()
    
    #Validacion de la consulta
    if country:
        #Validacion del metodo Get
        if request.method == 'GET' and pk is not None:
            country_serializer = CountriesSerializer(country)
            return Response(country_serializer.data, status=status.HTTP_200_OK)
        #Validacion del metodo Put
        elif request.method == 'PUT'and pk is not None:
            country = Countries.objects.filter(pk=pk).first()
            countries_serializer = CountriesSerializer(country, data=request.data )
            #Validacion de serializador
            if countries_serializer.is_valid():
                countries_serializer.save()
                return Response(countries_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE'and pk is not None:
            country.delete()
            return Response('Eliminado', status=status.HTTP_200_OK)
        
# Vista para idiomas    
@api_view(['GET', 'POST'])
def language_api_view(request):

    language = Languages.objects.all()
    
    #Validacion de datos|
    if language:
        #validacion de Metodo Get
        if request.method == 'GET':          
            language_serializer = LanguageSerializer(language, many=True)
            return Response(language_serializer.data, status=status.HTTP_200_OK)
        #Validcion del metodo Post
        elif request.method == 'POST':
            language_serializer = LanguageSerializer(data = request.data)
            if language_serializer.is_valid():
                language_serializer.save()
                return Response(language_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(language_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'Bad request'}, status=status.HTTP_400_BAD_REQUEST) 
    
# Vista para detalles, edicion y eliminado de idiomas
@api_view(['GET', 'PUT','DELETE'])
def detail_language_api_view(request, pk):
    #Consulta a base de datos
    language = Languages.objects.filter(pk=pk).first()
    # Validacion de consulta
    if language:
        # Validacion de Method
        if request.method == 'GET':
            language_serializer = LanguageSerializer(language)
            return Response(language_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            language_serializer =  LanguageSerializer(language, data=request.data, partial=True)
            if language_serializer.is_valid():
                language_serializer.save()
                return Response(language_serializer.data, status=status.HTTP_201_CREATED)
            return Response(language_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            language.delete()
            return Response({'message':'eliminacion exitosa'})
    else:
        return Response({'message':'BAD REQUEST'})


# viasta para Floor
    
@api_view(['GET', 'POST'])
def floor_api_view(request):
    floor = Floor.objects.all()
    if floor:
        if request.method == 'GET':
            floor_serializer = FloorSerializer(floor, many=True)
            return Response(floor_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            floor_serializer = FloorSerializer(data=request.data)
            if floor_serializer.is_valid():
                floor_serializer.save()
                return Response(floor_serializer.data, status=status.HTTP_201_CREATED)
        
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
# vista de floor para detalles, post, put y delete    
@api_view(['GET','POST','PUT','DELETE'])
def detail_floor_api_view(request, pk):
    floor = Floor.objects.filter(pk=pk).first()
    if floor:
        # Verificacion de metodos
        if request.method == 'GET':
            floor_serializer = FloorSerializer(floor)
            return Response(floor_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            floor_serializer = FloorSerializer(floor, data=request.data)
            return Response(floor_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            floor.delete()
            return Response({'message':'Elemento eliminado'})
    else:
        return Response({'message':'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

# vistas de museo

@api_view(['GET', 'POST'])
def museum_api_view(request):
    museums = Museum.objects.all()
    if museums:

        #validacion de methods

        if request.method == 'GET':
            museums_serializer = MuseumSerializer(museums,many=True)
            return Response(museums_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            museums_serializer =MuseumSerializer(museums_serializer, data=request.data)
            return Response(museums_serializer.data, status= status.HTTP_200_OK)
    else:
        return Response({'message':'BAD REQUEST'}, status= status.HTTP_400_BAD_REQUEST)

# Vistas de detalle, PUT y DELETE
    
@api_view(['GET', 'PUT', 'DELETE'])
def detail_museum_api_view(request, pk):
    museum =Museum.objects.filter(pk=pk).first()
    if museum:
        # Validacion de Method
        if request.method == 'GET':
            museum_serializer =  MuseumSerializer(museum)
            return Response(museum_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            museum_serializer =  MuseumSerializer(museum.data, data=request.data)
            return Response(museum_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            museum.delete()
            return Response({'message':'Elemento eliminado'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
    
# Viewsets de los modelos
class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountriesSerializer
    queryset = CountriesSerializer.Meta.model.objects.all()


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Languages.objects.all()

class FloorViewSet(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = FloorSerializer.Meta.model.objects.all()

class MuseumViewSet(viewsets.ModelViewSet):
    serializer_class = MuseumSerializer
    queryset = MuseumSerializer.Meta.model.objects.all()


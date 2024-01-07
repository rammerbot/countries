from rest_framework import serializers
from .models import Countries, Languages, Floor, Museum

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('__all__')

    def to_representation(self, instance):
        
        return {
            'ID': instance.id,
            'Pais':instance.country,
            'Bandera':instance.flag.url
        }


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('__all__')

# class LanguageSerializer(serializers.Serializer):

#     name = serializers.CharField(max_length=20)

#     def validate_name(self, value):
#         if value == '':
#             raise serializers.ValidationError("El campo no puede estar vacio")
#         return value

#     def validate(self, data):
#         pass
#         return data

#     def create(self, validated_data):
#         return Languages.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('__all__')

class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ('__all__')

    def to_representation(self, instance):

        return {
            'Museo':instance.name,
            'Pais':instance.country.country,
            'Idiomas':[language.name for language in instance.language.all()],
            'Piso':[floor.name for floor in instance.floor.all()],
            'Imagen':instance.image.url

        }

# class CountriesSerializer(serializers.Serializer):

#     country = serializers.CharField(max_length=50)
#     flag = serializers.ImageField()

#     def validate_country(self, value):
#         if value == '' or value == None:
#             raise serializers.ValidationError({'El campo no puede quedar en blanco'})
#         return value
#     def validate__flag(self, value):
#         if value == '' or value == None:
#             raise serializers.ValidationError({'El campo no puede quedar en blanco'})
#         elif value == str:
#             pass
#             return value
        
#     def validate(self, data):
#             return data
    
#     def create(self, validated_data):
#         return Countries.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         for inst in instance:
#             instance[inst] = validated_data.get(inst,instance[inst])
#         instance.save()
#         return instance
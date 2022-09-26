#
from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import Hobby, Person, Reunion

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

class PersonaSerializer(serializers.Serializer): # No trabaja directamente con  un modelo
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False)


class PersonaSerializer2(serializers.ModelSerializer):

    activo = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')

class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer() #Para poder mostrar todos los datos de un modelo en un serializador
    # simplemente igualo el atributo a un serializador que ya existe  exclusivamente para ese modelo y muestre todos los datos del modelo
    
    class Meta:
        model = Reunion
        # fields = ('__all__')
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )

class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('__all__')

class PersonaSerializer3(serializers.ModelSerializer):

    hobbies = HobbySerializer(many =True) #no olvidar los ()
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )
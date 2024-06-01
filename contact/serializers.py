from rest_framework import serializers

from .models import Contact


class SearchSerialize(serializers.Serializer):
    search = serializers.CharField(max_length=50)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    '''serializador do model Contact'''
    class Meta:
        model = Contact
        fields = [
            'id', 'url', 'first_name', 'last_name', 'phone', 'email',
            'description', 'show', 'picture', 'category'
        ]

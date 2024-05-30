from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    '''serializador do model Contact'''
    class Meta:
        model = Contact
        fields = [
            'id', 'url', 'first_name', 'last_name', 'phone', 'email',
            'description', 'show', 'picture', 'category'
        ]

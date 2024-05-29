from rest_framework import serializers

from .models import Category, Contact


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    '''serializador da do model Category'''

    class Meta:
        model = Category
        fields = ['id', 'url' 'name', ]


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    '''serializador do model Contact'''
    class Meta:
        model = Contact
        fields = [
            'id', 'url', 'first_name', 'last_name', 'phone', 'email',
            'description', 'show', 'picture', 'category'
        ]

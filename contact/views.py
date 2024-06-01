from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view

from .models import Contact
from .serializers import ContactSerializer, SearchSerialize


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)


@api_view(['POST', 'GET'])
def search(request):
    if request.method == 'GET':
        serializer = SearchSerialize()
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SearchSerialize(data=request.data)
        # search_values = request.GET.get('q', '').strip()
        if serializer.is_valid():
            search_values = serializer.data.get('search', '').strip()
            contacts = Contact.objects\
                .filter(show=True)\
                .filter(
                    Q(first_name__icontains=search_values) |
                    Q(last_name__icontains=search_values) |
                    Q(phone__icontains=search_values) |
                    Q(id__icontains=search_values) |
                    Q(email__icontains=search_values)
                )\
                .order_by("first_name")

            serializer = ContactSerializer(
                contacts, many=True, context={'request': request})
        return Response(serializer.data)

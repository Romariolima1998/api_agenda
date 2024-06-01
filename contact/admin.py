from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import Contact

admin.site.register(Contact)
admin.site.register(Token)

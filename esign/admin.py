from django.contrib import admin

# Register your models here.
from .models import changerequest
from .models import client

admin.site.register(changerequest)
admin.site.register(client)
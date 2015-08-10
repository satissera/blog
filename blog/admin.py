from django.contrib import admin

# Register your models here.
from blog.models import Entrada, Mensajes
admin.site.register(Entrada)
admin.site.register(Mensajes)

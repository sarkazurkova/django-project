from django.contrib import admin
from .models import Autor, Kniha, Druh, Zanr, Vydavatelstvi

# Register your models here.
admin.site.register(Autor)
admin.site.register(Druh)
admin.site.register(Zanr)
admin.site.register(Vydavatelstvi)
admin.site.register(Kniha)

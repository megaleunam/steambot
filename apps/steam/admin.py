from django.contrib import admin
from apps.steam.models import SearchItemExteriores, SearchItems, Armas, Exteriores, Resultados

# Register your models here.
admin.site.register(SearchItems)

admin.site.register(SearchItemExteriores)

admin.site.register(Armas)
admin.site.register(Resultados)
admin.site.register(Exteriores)

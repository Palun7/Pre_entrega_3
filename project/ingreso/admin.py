from django.contrib import admin

from ingreso.models import Ingreso, Usuario, Egreso

admin.site.register(Ingreso)
admin.site.register(Usuario)
admin.site.register(Egreso)

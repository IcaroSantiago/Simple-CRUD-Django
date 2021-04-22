from django.contrib import admin
from .models import Produtos

admin.site.register(Produtos)
class ViewAdmin(admin.ModelAdmin):
    pass


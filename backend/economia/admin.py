from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import  Continent, Currencie, Countrie
# Register your models here.




@admin.register(Continent)
class ContinentAdmin(ImportExportModelAdmin):


	list_display = ['id','region','subregion']



@admin.register(Currencie)
class CurrencieAdmin(ImportExportModelAdmin):


	list_display = ['id','name','symbol']


@admin.register(Countrie)
class CountrieAdmin(ImportExportModelAdmin):


	list_display = ['id','name','capital','official']



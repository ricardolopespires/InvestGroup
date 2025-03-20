from import_export.admin import ImportExportModelAdmin
from .models import CryptoAPI, MT5API , Broker, Account
from django.contrib import admin

# Register your models here.



@admin.register(CryptoAPI)
class APICryptoAdmin(ImportExportModelAdmin):
    list_display = ["name", "api_key", "api_secret", "endpoint", "broker_name", "created_at"]
    search_fields = ["name", "broker_name"]
    list_filter = ["name", "broker_name", "created_at"]



@admin.register(MT5API)
class MT5APIAdmin(ImportExportModelAdmin):
    list_display = ["broker_name", "login", "password", "server", "created_at"]
    search_fields = ["broker_name", "login"]
    list_filter = ["broker_name", "created_at"]


@admin.register(Broker)
class BrokerAdmin(ImportExportModelAdmin):
    list_display = ["name", "image", "created_at", "updated_at"]
    search_fields = ["name"]
    list_filter = ["name", "created_at", "updated_at"]
    
    

@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    list_display = ["id","nome"]
    search_fields = ["nome"]
    list_filter = ["nome"]
    




{
    "name":"",
    "image":"",
    "tipo_conta":[]
}
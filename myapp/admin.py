from django.contrib import admin
from .models import *
# Register your models here.


#this is for admin's columns display defined
""" 
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')


admin.site.register(YourModel, YourModelAdmin)

"""    
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']

class FactoryAdmin(admin.ModelAdmin):
    list_display = ['factory_name']

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name_ch','name_EN','name_Indonesian','food_types','Custom_unit','Custom_price','factory_name','Factory_unit','Factory_price')
    list_filter = ['factory_name']
    fieldsets = (
        ('商品名稱', {
            'fields': ('name_ch', 'name_EN', 'name_Indonesian','menu_picture','food_types')
        }),
        ('販售', {
            'fields': ('Custom_unit', 'Custom_price')
        }),
        ('廠商', {
            'fields': ('factory_name', 'Factory_unit','Factory_price')
        }),
    )

class StoreAdmin(admin.ModelAdmin):
    list_display = ('Store_ID','store_name','address','phone')
    list_filter = ['Store_ID']
    
    


admin.site.register(Menu,MenuAdmin)
admin.site.register(Factory,FactoryAdmin)
admin.site.register(Food_types,FoodTypeAdmin)
admin.site.register(store,StoreAdmin)
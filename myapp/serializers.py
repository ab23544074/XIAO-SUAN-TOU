from django.utils.timezone import now
from rest_framework import serializers
from myapp.models import *


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()


class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    singer = ToUpperCaseCharField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')

    def get_days_since_created(self, obj):
        return (now() - obj.created).days


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        # fields = '__all__'
        fields = ('Store_ID', 'store_name', 'address', 'phone')



class MenuSerializer(serializers.ModelSerializer):
    
    menu_picture = serializers.ImageField(
            max_length=None, use_url=True
        )
    
    class Meta:
        model = Menu
        # fields = '__all__'
        fields = ('name_ch', 'name_EN', 'name_Indonesian','menu_picture','Custom_unit', 'Custom_price')

    

    



from django.db import models

# Create your models here.


def display_genre(self):
    """Create a string for the Genre. This is required to display genre in Admin."""
    return ', '.join(genre.name for genre in self.genre.all()[:3])

display_genre.short_description = 'Genre'
class Menu(models.Model):
    Menu_ID = models.AutoField(primary_key=True)
    name_ch = models.CharField(("商品名稱（中文）"), max_length=20,help_text='鹹酥雞')
    name_EN = models.CharField(("商品名稱（英文）"),max_length=50,help_text='Taiwanese fried chicken')
    name_Indonesian = models.CharField(("商品名稱（印尼文）"),max_length=100,help_text='Ayam Renyah Asin')
    menu_picture = models.ImageField(upload_to='static/images/', blank=True, null=True)
    factory_name = models.ForeignKey(
        'Factory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    Custom_unit = models.CharField(("販售單位"),max_length=10,help_text='份',blank=True)
    Custom_price = models.IntegerField(("販售價格"),help_text='50',blank=True,null=True)

    Factory_unit = models.CharField(("叫貨單位"),max_length=10,help_text='件',blank=True)
    Factory_price = models.IntegerField(("貨品價格"),help_text='560',blank=True,null=True)
    
    class Meta:
        ordering = ['Menu_ID']

    def __str__(self):
        return f'{self.name_ch},{self.name_EN},{self.name_Indonesian},{self.Custom_unit},{self.Custom_price},{self.factory_name},{self.Factory_unit},{self.Factory_price}'


class Factory(models.Model):
    Factory_ID = models.AutoField(primary_key=True)
    factory_name = models.CharField(("廠商名稱"),max_length=10)
    class Meta:
        ordering = ['Factory_ID']
    
    def __str__(self):
        return self.factory_name


class store(models.Model):
    Store_ID = models.AutoField(primary_key=True)
    store_name = models.CharField(("分店名稱"),max_length=10)
    address = models.CharField(("地址"),max_length=100)
    phone = models.CharField(("電話"),max_length=10)
    
    class Meta:
        ordering = ['Store_ID']
    
    def __str__(self):
        return self.store_name


class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"




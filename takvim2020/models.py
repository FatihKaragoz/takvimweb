from django.db import models
import uuid
import time
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

ORDER_STATUS = (
    (1,"Siparişin müşteri tarafından onaylanması bekleniyor(sepette)"),
    (2,"Sipariş tamamlandı kargolanması bekleniyor"),
    (3,"Kargoya verildi")
)

PRODUCT_CATEGORY = {
    ("gemicieko","GEMİCİ EKO"),
    ("gemici3","GEMİCİ 3 Spiral"),
    ("gemici2","GEMİCİ 2 Spiral"),
    ("gemici1","GEMİCİ 1 Spiral"),
    ("masaustu","MASAUSTU"),
    ("ajanda","AJANDA"),
}

PRODUCT_IMAGE_STATUS = (
    (1,"Büyük"),
    (2,"Küçük")
)

USERSTATUS = (
    (0,"Inaktif"),
    (1,"Aktif")
)


class menuC(models.Model):
    menu_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    menuItem = models.CharField(choices=PRODUCT_CATEGORY,max_length=50,verbose_name="category")
    menuExp = models.CharField(max_length=50,verbose_name="Menüde görülecek isim")
    ordering = models.IntegerField()
    image = models.ImageField(verbose_name="Menü Resmi")

    def __str__(self):
        return str(self.menu_id)

class colorname(models.Model):
    color_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    colorname = models.CharField(max_length=50,verbose_name="Renk ismi")

    def __str__(self):
        return self.colorname

class instagramgonderi(models.Model):
    gonderi_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    url = models.CharField(verbose_name="URL",max_length=5000)

    def __str__(self):
        return self.url
class color(models.Model):
    color2_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    exp = models.CharField(verbose_name="Renk açıklama",max_length=100)
    model = models.CharField(choices=PRODUCT_CATEGORY,max_length=50,verbose_name="Kategori")
    backimage = models.ImageField(verbose_name="Arka resim",blank=True)
    frontimage = models.ImageField(verbose_name="Ön resim")

    def __str__(self):
        return self.exp



class blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, blank=True, unique=True)
    caption = models.CharField(verbose_name="Başlık", max_length=100)
    contain = models.CharField(verbose_name="Yazı", max_length=1000)
    menuimage = models.ImageField(verbose_name="Küçük resim", blank=True)
    image = models.ImageField(verbose_name="Büyük resim", blank=True)
    keywords = models.CharField(max_length=50,verbose_name="Anahtar kelimeler")
    featured = models.CharField(max_length=50,verbose_name="Önerilen")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class contact(models.Model):
    contact_id=models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    fullname = models.CharField(max_length=60,verbose_name="Ad soyad",editable=False)
    message = models.CharField(max_length=1000,verbose_name="Mesaj",editable=False)
    email = models.EmailField(verbose_name="Email adresi")
    phone = models.CharField(max_length=50,verbose_name="Telefon numarası")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created

class price(models.Model):
    price_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    exp = models.CharField(max_length=100,verbose_name="Açıklama")
    model = models.CharField(choices=PRODUCT_CATEGORY,max_length=50,verbose_name="Model")
    price50_100 = models.DecimalField(verbose_name="Fiyat (50-100 adet için)",max_digits=4, decimal_places=2)
    price100_200 = models.DecimalField(verbose_name="Fiyat (100-200 adet için)",max_digits=4,decimal_places=2)
    price200_500 = models.DecimalField(verbose_name="Fiyat (200-500 adet için)",max_digits=4, decimal_places=2)
    price500_1000 = models.DecimalField(verbose_name="Fiyat (500-1000 adet için)",max_digits=4, decimal_places=2)
    price1000_2000 = models.DecimalField(verbose_name="Fiyat (1000-2000 adet için)",max_digits=4, decimal_places=2)
    price2000_5000 = models.DecimalField(verbose_name="Fiyat (2000-5000 adet için)",max_digits=4, decimal_places=2)
    priceDesignService = models.IntegerField(verbose_name="Tasarim hizmet bedeli")

    def __str__(self):
        return self.exp


class size(models.Model):
    size_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=50)
    name = models.CharField(max_length=50,verbose_name="Açıklama")
    size = models.CharField(max_length=50,verbose_name="Ölçüler")
    color1 = models.ForeignKey(color, verbose_name="Renk 1", related_name="renk1renk",on_delete=models.CASCADE)
    color2 = models.ForeignKey(color, verbose_name="Renk 2", related_name="renk2renk",on_delete=models.CASCADE,blank=True,null=True)
    price = models.ForeignKey(price, verbose_name="Fiyat",related_name="Fiyat2Fiyat",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

class userInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='MainUser')
    fullname = models.CharField(max_length=100,verbose_name="Isim soyisim",blank=True)
    address = models.CharField(max_length=200,verbose_name='adres',blank=True,null=True)
    phone = models.CharField(max_length=30,verbose_name="telefon",blank=True)
    comName = models.CharField(max_length=100,verbose_name="Sirket ismi",blank=True)
    dateofJoin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class gemici1(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="GEMİCİ 3 Spiral")
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=20,verbose_name="Kategori")
    exp = models.CharField(max_length=100,blank=True)
    size1 = models.ForeignKey(size,verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar ",related_name="OlcuGemici",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_id)

class gemici2(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="GEMİCİ 3 Spiral")
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=20,verbose_name="Kategori")
    exp = models.CharField(max_length=100,blank=True)
    size1 = models.ForeignKey(size,verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar ",related_name="OlcuGemici2",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)


class gemicieko(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="GEMİCİ 3 Spiral")
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=20,verbose_name="Kategori")
    exp = models.CharField(max_length=100,blank=True)
    size1 = models.ForeignKey(size,verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar ",related_name="OlcuGemiciEko",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)

class akademik(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, verbose_name="Kategori")
    exp = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50,default="AKADEMİK")
    size1 = models.ForeignKey(size, verbose_name="Boyut - Renk - Fotoğraf", related_name="OlcuAkademik",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)

class ajanda(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, verbose_name="Kategori")
    exp = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50,default="AJANDA")
    size1 = models.ForeignKey(size, verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar", related_name="Olcu1Ajanda",on_delete=models.CASCADE)
    size2 = models.ForeignKey(size, verbose_name="Ölçü 2 için  boyut - renk - fotoğraglar", related_name="Olcu2Ajan",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)


class masaustu(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, verbose_name="Kategori")
    exp = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50,default="MASAÜSTÜ")
    size1 = models.ForeignKey(size,verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar",related_name="Olcu1Masaustu",on_delete=models.CASCADE)
    size2 = models.ForeignKey(size, verbose_name="Ölçü 2 için boyut - renk - fotoğraflar",related_name="Olcu2Masaustu",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)


class gemici3(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    exp = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50,default="GEMİCİ 3 Spiral")
    category = models.CharField(choices=PRODUCT_CATEGORY,max_length=20,verbose_name="Kategori")

    size1 = models.ForeignKey(size,verbose_name="Ölçü 1 için  boyut - renk - fotoğraglar ",related_name="Olcu1Olcu",on_delete=models.CASCADE)
    size2 = models.ForeignKey(size, verbose_name="Ölçü 2 için boyut - renk - fotoğraflar",related_name="Olcu2Olcu",on_delete=models.CASCADE)
    size3 = models.ForeignKey(size, verbose_name="Ölçü 3 için boyut - renk - fotoğraflar",related_name="Olcu3Size",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_id)


class slider(models.Model):
    slider_id = models.UUIDField(primary_key=True, default=uuid.uuid4(),editable=False,blank=True,unique=True)
    yayinci = models.ForeignKey(User,on_delete=models.CASCADE)
    baslik = models.CharField(max_length=50,verbose_name="Slider Başlığı")
    aciklama = models.CharField(max_length=50,verbose_name="Slider Açıklama")
    image = models.ImageField(verbose_name="Slider Resmi")
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, verbose_name="Kategori")
    idd = models.IntegerField(verbose_name="Manu sıralaması")

    def __str__(self):
        return str(self.idd)

class siparis(models.Model):
    siparis_id = models.UUIDField(primary_key=True, default=uuid.uuid4(),editable=False,blank=True,unique=True)
    created_at = models.DateTimeField(default=timezone.now(),verbose_name="Siparis zamanı")
    fullname = models.CharField(max_length=50,verbose_name="Müşteri isim soyisim")
    comName = models.CharField(max_length=50,verbose_name="Şirket ismi")
    address = models.CharField(max_length=100,verbose_name="Adres")
    phone = models.CharField(max_length=50,verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-mail")
    color = models.CharField(max_length=50,verbose_name="Renk")
    size = models.CharField(max_length=50,verbose_name="Ölçüler")
    pieces = models.CharField(max_length=50,verbose_name="Adet")
    price = models.CharField(max_length=50,verbose_name="Adet fiyat")
    sumprice = models.CharField(max_length=50,verbose_name="Toplam fiyat")
    product_id = models.CharField(choices=PRODUCT_CATEGORY, max_length=20, verbose_name="Kategori")
    designService = models.CharField(max_length=5, verbose_name="Tasarım hizmeti verilecek mi?")

    design = models.ImageField(blank=True,verbose_name="Üst tasarım")
    design1 = models.ImageField(blank=True,verbose_name="Alt tasarım")

    def __str__(self):
        return str(self.siparis_id)
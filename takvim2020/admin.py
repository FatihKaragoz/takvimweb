from django.contrib import admin
from .models import menuC,colorname,size,color,price,userInformation,gemici3,gemici1,gemici2,gemicieko,akademik,masaustu,ajanda,blog,slider,siparis,contact,instagramgonderi

# Register your models here.
class menuAdmin(admin.ModelAdmin):
    list_display = ("menuItem","menuposition","image")
    list_filter = ("menuItem","menuposition")

admin.site.register(menuC,menuAdmin)

class colorNameAdmin(admin.ModelAdmin):
    list_display = ("colorname","color_id")

admin.site.register(colorname,colorNameAdmin)

class sizeAdmin(admin.ModelAdmin):
    list_display = ("category","size","name")

admin.site.register(size,sizeAdmin)

class colorAdmin(admin.ModelAdmin):
    list_display = ("exp","model","backimage","frontimage")
    list_filter = ("exp","backimage","frontimage")

admin.site.register(color,colorAdmin)

class priceAdmin(admin.ModelAdmin):
    list_display = ("model","price50_100","price100_200","price200_500","price500_1000","price1000_2000","price2000_5000","priceDesignService")
    list_filter = ("model","price_id")

admin.site.register(price,priceAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('fullname','address','phone','comName','dateofJoin')
    list_filter = ('comName','fullname','dateofJoin')
    search_fields =  ['fullname','comName','dateofJoin']

admin.site.register(userInformation,UserAdmin)

class gemici3admin(admin.ModelAdmin):
    list_display = ("name","category","author",
                    "size1",
                    "size2",
                    "size3" )
admin.site.register(gemici3,gemici3admin)

class gemici1admin(admin.ModelAdmin):
    list_display = ("name","category","author","size1")

admin.site.register(gemici1,gemici1admin)

class gemici2admin(admin.ModelAdmin):
    list_display = ("name","category","author","exp","size1")

admin.site.register(gemici2,gemici2admin)

class gemiciekoadmin(admin.ModelAdmin):
    list_display = ("name","category","author","exp","size1")

admin.site.register(gemicieko,gemiciekoadmin)


class masaustuadmin(admin.ModelAdmin):
    list_display = ("name","category","author","size1","size2")

admin.site.register(masaustu,masaustuadmin)

class akademikadmin(admin.ModelAdmin):
    list_display = ("name","category","author","size1")

admin.site.register(akademik,akademikadmin)

class ajandaadmin(admin.ModelAdmin):
    list_display = ("name","category","author","size1","size2")

admin.site.register(ajanda,ajandaadmin)

class blogAdmin(admin.ModelAdmin):
    list_display = ("caption","contain","menuimage","image")

admin.site.register(blog,blogAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ("fullname","email","phone","message")

admin.site.register(contact,contactAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ("baslik","aciklama","category","slider_id")

admin.site.register(slider,SliderAdmin)

class SiparisAdmin(admin.ModelAdmin):
    list_display = ("fullname","comName","address","phone","email","color","size","pieces","product_id","design","design1","price",'sumprice','designService')

admin.site.register(siparis,SiparisAdmin)

class instagramGonderiAdmin(admin.ModelAdmin):
    list_display = ("gonderi_id","url")

admin.site.register(instagramgonderi,instagramGonderiAdmin)
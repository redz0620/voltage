from django.contrib import admin
from . models import *
# from . models import Contact, Product, Profile

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','email','message','admin_note','status','message_date','admin_update')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','img','price','max_quantity','min_quantity','display','latest','trending','created','update']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'phone', 'address', 'state', 'pix']

class ShopcartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'name_id', 'quantity', 'price', 'amount', 'order_no', 'paid', 'created_at')





admin.site.register(Contact,ContactAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Shopcart,ShopcartAdmin)




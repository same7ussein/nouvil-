from django.contrib import admin
from .models import Category,Book



 
admin.site.register(Category)
admin.site.register(Book)
admin.site.site_title='Nouvil'
admin.site.site_header='Nouvil'  

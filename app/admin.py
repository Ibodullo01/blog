from django.contrib import admin


from .models import Category, Blog, Comments


admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comments)

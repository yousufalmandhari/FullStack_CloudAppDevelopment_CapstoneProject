from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.StackedInline):
    model = CarModel
    extra = 5

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake)

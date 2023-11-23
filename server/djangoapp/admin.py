from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
  model = CarModel

class CarMakelAdmin(admin.ModelAdmin):
  inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)

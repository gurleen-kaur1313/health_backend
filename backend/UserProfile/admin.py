from UserProfile.schema import UserProfile
from django.contrib import admin
from .models import UserProfile,DailyNutritions
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(DailyNutritions)
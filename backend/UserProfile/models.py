from django.db import models
import uuid
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class UserProfile(models.Model):
    """Model to store user profile data"""

    gender_choices = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, default="User",
                            blank=True, max_length=255)
    gender = models.CharField(
        null=True, blank=True, choices=gender_choices, max_length=6,default="M")
    image = models.URLField(
        null=True, default="https://firebasestorage.googleapis.com/v0/b/duo-louge.appspot.com/o/user_default.png?alt=media&token=a27eb92b-8292-4e0c-84d3-5db84b1b18d0")
    age = models.IntegerField(default=1, validators=[
                              MinValueValidator(1), MaxValueValidator(100)])
    weight = models.IntegerField(validators=[
        MinValueValidator(0)])
    height = models.IntegerField(validators=[
        MinValueValidator(0)])
    bmi = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    max_score = models.IntegerField(default=0, validators=[
        MinValueValidator(0)])
    game_life = models.IntegerField(default=3, validators=[
        MinValueValidator(0)])
    nutrition = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.user.email


class DailyNutritions(models.Model):
    """model to store daily nutrition intake of the user"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now=True, blank=True)
    protein = models.CharField(null=True, blank=True, max_length=20)
    carbs = models.CharField(null=True, blank=True, max_length=20)
    fats = models.CharField(null=True, blank=True, max_length=20)
    food_name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.user.email



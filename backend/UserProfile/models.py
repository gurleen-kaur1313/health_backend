from django.db import models
import uuid
from django.conf import settings
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
        null=True, blank=True, choices=gender_choices, max_length=6)
    image = models.URLField(
        null=True, default="https://firebasestorage.googleapis.com/v0/b/duo-louge.appspot.com/o/user_default.png?alt=media&token=a27eb92b-8292-4e0c-84d3-5db84b1b18d0")
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.email

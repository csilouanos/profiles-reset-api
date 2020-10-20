from django.contrib import admin
from profiles_api import models

# Registers the UserProfile model as admin
admin.site.register(models.UserProfile)

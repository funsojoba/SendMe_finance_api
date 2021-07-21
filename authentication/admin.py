from django.contrib import admin

from .models.user import User
from .models.balance import Balance

admin.site.register((User, Balance))

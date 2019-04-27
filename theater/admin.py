from django.contrib import admin
from .models import (
    HallType, Hall, ScreenTime, ScreenDay, ShowTime)

admin.site.register(HallType)
admin.site.register(Hall)
admin.site.register(ScreenDay)
admin.site.register(ScreenTime)
admin.site.register(ShowTime)

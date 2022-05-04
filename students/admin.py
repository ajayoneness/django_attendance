from django.contrib import admin
from .models import students,teachers,presentabsent



admin.site.register(students)
admin.site.register(teachers)
admin.site.register(presentabsent)

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name = 'home'),
    path('student/',views.student ,name='student'),
    path('submit',views.submit , name='submit'),
    path('search/',views.search , name='search'),
    path('contact/',views.contact ,name = 'contact'),
    path('attendance/',views.attendance ,name = 'attendance'),
    path('download/',views.download ,name = 'download'),
]

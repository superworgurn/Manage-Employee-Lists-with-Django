from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/',admin.site.urls), #เข้าดูหลังบ้าน
    path('',include('person.urls')),
]
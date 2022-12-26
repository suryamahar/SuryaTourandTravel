from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Surya Icecream Admin"
admin.site.site_title = "Surya Icecream  Admin Portal"
admin.site.index_title = "Welcome to Surya Icecream  Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('about',include('home.urls')),
    path('services',include('home.urls')),
    path('contact',include('home.urls'))

]



"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from products.views import calculator, random, datatables, google_file_upload, table, loading_bar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('auth/', include('allauth.urls')),
    #path('home/', home, name='home'),
    path('', include('products.urls')),
    path('profile/', profile, name='profile'),
    path('loadingbar/', loading_bar, name='loadingbar'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('address_details/', address_details, name='address_details'),
    path('edit_address/<id>', edit_address, name='edit_address'),
    path('calculator/', calculator, name='calculator'),
    path('random/', random, name='random'),
    path('table/', table, name='table'),
    path('datatables/', datatables, name='datatables'),
    path('google_file_upload/', google_file_upload, name='google_file_upload'),
    path('admin/', admin.site.urls),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

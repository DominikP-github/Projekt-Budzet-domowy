"""
URL configuration for Projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kategorie/', views.kategorie_view, name='kategorie_view'),
    path('update-realization/<int:tranzakcja_id>/', views.update_realization, name='update_realization'),
    path('login/', views.user_login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('', views.home, name='home'),
    path('logout/',views.logout_page,name='logout'),
    path('dodaj_kategorie/', views.dodaj_kategorie, name='dodaj_kategorie'),
    path('dodaj_podkategorie/', views.dodaj_podkategorie, name='dodaj_podkategorie'),
    path('kategoria/edytuj/<int:kategoria_id>/', views.edytuj_kategorie, name='edytuj_kategorie'),
    path('update-realization/', views.update_realization, name='update_realization'),
    path('tranzakcja/edytuj/<int:tranzakcja_id>/', views.edytuj_podkategorie, name='edytuj_podkategorie'),
    path('kategorie/usun/<int:kategoria_id>/', views.usun_kategorie, name='usun_kategorie'),
    path('podkategorie/usun/<int:tranzakcja_id>/', views.usun_podkategorie, name='usun_podkategorie'),
    path('roczny_raport/', views.roczny_wykres, name='roczny_wykres'),
]



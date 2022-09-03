"""mysite URL Configuration

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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from registration.views import RegistrationList
from riarest.views import CitiesList, AppartmentsList, AppartmentsDetail, CitiesDetail, OwnersList, OwnersDetail, Logout
from knox import views as knox_views

urlpatterns = [
    path('registration/', RegistrationList.as_view()),
    path('login/', obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/appartments/', AppartmentsList.as_view()),
    path('api/v1/appartments/<int:pk>/', AppartmentsDetail.as_view()),
    path('api/v1/cities/', CitiesList.as_view()),
    path('api/v1/cities/<int:pk>/', CitiesDetail.as_view()),
    path('api/v1/owners/', OwnersList.as_view()),
    path('api/v1/owners/<int:pk>/', OwnersDetail.as_view())

]

from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', views.api)

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('sinup/',views.sinup, name='sinup'),
    path('logout/',views.logout, name='logout'),
    # path('form/', views.form_post, name='form_post'),
    path('',include(router.urls)),
]

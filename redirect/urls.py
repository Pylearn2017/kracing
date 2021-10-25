from django.urls import path
from . import views

urlpatterns = [
    path('', views.RedirectPage.as_view(), name='redirect')
]
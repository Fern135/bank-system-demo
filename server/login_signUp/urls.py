from django.urls import path
from . import views

urlpatterns = [
    path("api/controllers/security/get_csrf",   views.index, name="index"), # may need to change this
    path('api/controllers/user/login/',         views.login, name='login'),
    path('api/controllers/user/signUp/',        views.signUp, name='signUp'),
    path('api/controllers/user/forgot/',        views.forgot, name='forgot'),
]

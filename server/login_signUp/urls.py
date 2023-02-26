from django.urls import path
from .views import login, signUp, forgot, index

urlpatterns = [
    path("", index, name="index"),
    path('api/controllers/user/login/', login, name='login'),
    path('api/controllers/user/signUp/', signUp, name='signUp'),
    path('api/controllers/user/forgot/', forgot, name='forgot'),
]

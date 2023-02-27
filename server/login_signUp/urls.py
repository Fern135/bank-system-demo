from django.urls import path
from .views import login, signUp, forgot, index

urlpatterns = [
    path("api/controllers/security/get_csrf", index, name="index"), # may need to change this
    path('api/controllers/user/login/', login, name='login'),
    path('api/controllers/user/signUp/', signUp, name='signUp'),
    path('api/controllers/user/forgot/', forgot, name='forgot'),
]

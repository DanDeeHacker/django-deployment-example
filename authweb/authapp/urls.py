from django.urls import re_path
from . import views

app_name='authapp'

urlpatterns=[
    re_path(r'^registration/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login')
]

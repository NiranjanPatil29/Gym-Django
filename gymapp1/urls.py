from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('get',views.get,name='get'),
    path('update',views.update,name='update'),
    path('cancel',views.cancel,name='cancel'),
    path('logout',views.logout,name="logout"),
    path('congrats',views.congrats,name="congrats"),
]
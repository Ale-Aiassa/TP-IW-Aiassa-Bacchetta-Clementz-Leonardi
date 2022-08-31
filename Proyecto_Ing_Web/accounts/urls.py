from django.urls import path

from .views import SecondPage, home2, home, login, signup #SignUpView,


urlpatterns = [
    #path("signup/", SignUpView.as_view(), name="signup"),
    path('home2/', home2, name="home2"),
    path('', home, name="home"),
    path('SecondPage/', SecondPage, name="SecondPage"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
]
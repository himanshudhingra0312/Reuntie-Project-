from django.urls import path,include
from .import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/',views.profile,name='users-profile'),
    path('thanks/',views.thanks,name="thanks")

]

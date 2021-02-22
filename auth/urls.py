from django.urls import path,include

from auth.views import landing

urlpatterns = [
    path('Login/', landing.SigninView.as_view(),name="signin"),
    path('Logout/', landing.logoutHome,name="logout"),

]

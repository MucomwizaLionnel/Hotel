
from django.urls import path
from Agence.views import home,login,gerant,caissiere,register,touriste



urlpatterns = [

    path('',home ,name="home" ),
    path('login',login ,name='login' ),
    path('register/',register ,name='register' ),
    path('gerant/',gerant ,name='gerant' ),
    path('caissiere/',caissiere ,name='caissiere' ),
    path('touriste/',touriste ,name='touriste' ),



]

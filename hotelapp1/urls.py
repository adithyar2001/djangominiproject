from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('loginop/',views.loginop,name="loginop"),
    path('signupop/',views.signupop,name="signupop"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('guestsignup/',views.guestsignup,name="guestsignup"),
    path('guestlogin/',views.guestlogin,name="guestlogin"),
    path('guestloginfunc/',views.guestloginfunc,name="guestloginfunc"),
    path('guestprofile/',views.guestprofile,name="guestprofile"),
    path('guestupdate/<str:pk>',views.guestupdate,name="guestupdate"),
    path('deleteguest/<str:pk>',views.deleteguest,name="deleteguest"),
    path('guestlogout/',views.guestlogout,name="guestlogout"),
    path('staffsignup/',views.staffsignup,name="staffsignup"),
    path('stafflogin/',views.stafflogin,name="stafflogin"),
    path('staffloginfunc/',views.staffloginfunc,name="staffloginfunc"),
    path('staffprofiles/',views.staffprofiles,name="staffprofiles"),
    path('staffupdate/<str:pk>',views.staffupdate,name="staffupdate"),
    path('deletestaff/<str:pk>',views.deletestaff,name="deletestaff"),
    path('stafflogout/',views.stafflogout,name="stafflogout"),
    path('addroom/',views.addroom,name="addroom"),
    path('roomupdate/<str:pk>',views.roomupdate,name="roomupdate"),
    path('bookrooms/',views.bookrooms,name="bookrooms"),
    path('bookingroom/',views.bookingroom,name="bookingroom"),
    path('checkbooking/',views.checkbooking,name="checkbooking"),
    path('staffviewforupdate/',views.staffviewforupdate,name="staffviewforupdate"),
    path('approveroom/<str:pk>',views.approveroom,name="approveroom"),
    path('guestbookingstatus/',views.guestbookingstatus,name="guestbookingstatus"),
]

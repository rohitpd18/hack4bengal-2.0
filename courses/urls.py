
from django.contrib import admin
from django.urls import path , include
from courses.views import  MyCoursesList,  HomePageView ,verifyPayment , coursePage, signup  , login_view , signout , checkout, profile,creater, become_creater
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('signup', signup , name = 'signup'),
    path('login', login_view , name = 'login'),
    path('logout', signout , name = 'logout'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('profile', profile , name = 'profile'),
    path('creater', creater, name = 'creater'),
    path('become_creater', become_creater , name = 'become_creater'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.contrib import admin
from django.urls import path
from profileapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myinfo', views.myinfo, name='myinfo'),
    path('education', views.education, name='education'),
    path('interest', views.interest, name='interest'),
    path('career', views.career, name='career'),
    path('idol', views.myidols, name='idol'),
    path('etc', views.etc, name='etc'),
    path('lab10', views.lab10, name="lab10"),
]
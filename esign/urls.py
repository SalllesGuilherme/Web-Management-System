from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage,name="home"),
    path('projects/',views.project,name="projects"),
    path('main/',views.main),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('about/',views.about)

]

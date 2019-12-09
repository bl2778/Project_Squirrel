from django.urls import path

from . import views

app_name='sightings'

urlpatterns = [
    path('',views.all_squirrels,name='index'),
    path('list/', views.all_squirrels,name='list'),
    path('map/',views.map),
    path('add/', views.add_squirrel),
    path('stats/',views.stats),
    path('<Unique_squirrel_id>/', views.edit_squirrel),
]


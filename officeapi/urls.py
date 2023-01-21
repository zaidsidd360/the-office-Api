from django.contrib import admin
from django.urls import path
from officeapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', views.get_characters),
    path('characters/<str:_id>', views.get_character),
    path('seasons/', views.get_seasons),
    path('seasons/<str:s_id>', views.get_season),
    path('bestepisodes/', views.get_bestepisodes),
]

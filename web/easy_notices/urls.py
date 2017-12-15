from django.urls import path
from . import views

app_name = 'easy_notices'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]

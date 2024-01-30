from .views import home, detail
from django.urls import path

urlpatterns = [
    path("<int:pk>", home),
    path('detail/<int:pk>', detail),
]

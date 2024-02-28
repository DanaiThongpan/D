from django.urls import path

from .views import home, up

urlpatterns = [
    path('', home),
    path('up/<int:id>/', up),
]

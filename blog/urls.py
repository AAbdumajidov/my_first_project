from django.urls import path
from .views import index

app_name = "blogs"

urlpatterns = [
    path('', index, name="list")
]
from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [path("", views.base_view, name="home")]

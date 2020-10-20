from django.urls import path

from profiles_api import views

#.as_view converts the HelloApiView to view
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
]

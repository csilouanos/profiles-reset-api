from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#Router will create all the urls for us
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#We don't need to specify a basename attribute because we have declared (in UserProfileViewSet)
#a queryset
router.register('profile', views.UserProfileViewSet)

#.as_view converts the HelloApiView to view
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    #we don't want to include a prefix for this url
    path('', include(router.urls))
]

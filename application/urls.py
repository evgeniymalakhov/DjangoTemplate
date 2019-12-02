from django.urls import path

from application.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
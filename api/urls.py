
from django.urls import path
from api import views

urlpatterns = [
    path('resume/',  views.ProfileCreateView.as_view(), name='resune'),
    path('list/',  views.ProfileCreateView.as_view(), name='list'),
]

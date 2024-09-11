from django.urls import path
from .views import get_recommendation

urlpatterns = [
    path('<int:recommendation_id>/', get_recommendation),
]

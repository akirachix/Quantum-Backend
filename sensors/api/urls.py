from django.urls import path
from .views import RecommendationListView, InactiveSensorsListView, PhReadingsListView

urlpatterns = [
  
    path('recommendation/', RecommendationListView.as_view(), name='recommendation-list'),
    
    path('inactive/', InactiveSensorsListView.as_view(), name='get_inactive_sensors'),

    
    path('ph-readings/', PhReadingsListView.as_view(), name='list_ph_readings'),

    
 
]

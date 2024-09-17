from django.urls import path
from .import views 
from .views import FarmerListView

urlpatterns = [
    path('send_recommendation/<int:farmer_id>/', views.send_recommendation, name='send_recommendation'),
    path('farmer/<int:farmer_id>/', views.farmer_detail, name='farmer_detail'),
    path('farmers/', FarmerListView.as_view(), name='farmer-list'),

]







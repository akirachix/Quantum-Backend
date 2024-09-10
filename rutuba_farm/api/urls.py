from django.urls import path
from .views import PhreadingsListView
from .views import PhreadingsDetailView
urlpatterns = [
    path('phreadings/',PhreadingsListView.as_view(),name='phreadings_list_view'),
    path('phreadings/<int:id>', PhreadingsDetailView.as_view(),name='phreadings_list_view'),
]
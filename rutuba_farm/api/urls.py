from django.urls import path
from .views import NpkReadingListView, RecommendationsListView,NpkReadingDetailView,RecommendationsDetailView


urlpatterns = [
    path("npkreading/", NpkReadingListView.as_view(), name="npkreading_list_view"),
    path("recommendations/", RecommendationsListView.as_view(), name="recommendations_list_view"),
    path("npkreading/<int:id>/",NpkReadingDetailView.as_view(),name="npkreadingdetail_view"),
    path("recommendations/<int:id>/",RecommendationsDetailView.as_view(),name="recommendationsdetail_view"),
]

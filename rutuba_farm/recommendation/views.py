from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Recommendation
# from .serializers import RecommendationSerializer
from rest_framework import status

@api_view(['GET'])
def get_recommendation(request, recommendation_id):
    try:
        recommendation = Recommendation.objects.get(id=recommendation_id)
        # serializer = RecommendationSerializer(recommendation)
        # return Response(serializer.data)
    except Recommendation.DoesNotExist:
        return Response({"error": "Recommendation not found"}, status=status.HTTP_404_NOT_FOUND)


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from farmer.models import Farmer
from sendsms.models import Sendsms
from sendsms.utils import send_sms
import random

@api_view(['POST'])
def send_sms_view(request):
    phone_number = request.data.get('phone_number')  
    if not phone_number:
        return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        farmer = get_object_or_404(Farmer,phone_number=phone_number)

        message = f"Hello {farmer.farmers_name}, here are your recommendations: [YOUR_RECOMMENDATIONS_HERE]"

        response = send_sms(phone_number, message) 

        if response:
            # Save to database
            Sendsms.objects.create(
                sender_id=random.randint(1000, 9999),  
                recipient=phone_number,
                farmer_id=farmer.farmer_id,
                sensor_id=0,
                message=message
            )
            return Response({"status": "SMS sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to send SMS"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        print(f"An error occurred: {str(e)}")  
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


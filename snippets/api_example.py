# api_example.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Simple API endpoint for reporting fire incidents
@csrf_exempt
def report_incident(request):
    if request.method == "POST":
        data = json.loads(request.body)
        incident = {
            "location": data.get("location", "Unknown"),
            "type": data.get("type", "Fire"),
            "reporter": data.get("reporter", "Anonymous"),
            "status": "Received"
        }
        # Normally, this would be saved to PostgreSQL
        return JsonResponse({"message": "Incident reported successfully", "incident": incident})
    return JsonResponse({"error": "Invalid request"}, status=400)

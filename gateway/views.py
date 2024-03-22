import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import process_request


@csrf_exempt
def gateway(request):
    if request.method == "POST":
        try:
            headers = dict(request.headers)
            request.session["processed"] = True
            result = process_request.apply_async(
                args=[json.dumps(headers), request.body]
            )
            response = JsonResponse(
                {"message": "Request accepted and processed."}, status=200
            )
            response["X-Celery-ID"] = result.id
            return response
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Error"}, status=200)

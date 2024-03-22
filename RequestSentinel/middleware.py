from django.core.cache import cache

from django.http import HttpResponse


class DuplicateRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_body = request.body

        headers = request.headers

        request_data = {
            "body": request_body.decode(),
            "headers": str(headers),
        }
        if cache.get(request_data):
            return HttpResponse(status=200)
        cache.set(request_data, True)
        response = self.get_response(request)

        return response

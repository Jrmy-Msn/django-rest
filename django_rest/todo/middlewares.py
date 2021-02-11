from django.conf import settings

class ModifyHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.headers = {**request.headers, **settings.SIMULATE_HEADERS}
        response = self.get_response(request)
        return response
# from django.urls import resolve
import sentry_sdk


class Sentry404Middleware:
    """
    class to send to Sentry unavailable page tried to be accessed
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            sentry_sdk.capture_message(f"Page not found: {request.path_info}")
        return response

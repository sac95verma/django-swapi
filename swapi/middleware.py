from django.http import HttpResponseForbidden

class SecretTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        secret_token = 'your_secret_token'  # Replace with your actual secret token
        excluded_paths = ['/swapi/people/rate']
        if request.path in excluded_paths:
        # Check if the secret token is present in the Authorization header
            authorization_header = request.headers.get('Authorization', '')
            if authorization_header != f'Token {secret_token}':
                response = HttpResponseForbidden()
                return response

        return self.get_response(request)

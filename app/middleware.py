from django.contrib.auth.models import User

class AddUsersToResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if response.status_code == 200:
            users = User.objects.all()
            response.context_data['users_middleware'] = users

        return response

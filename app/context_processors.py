from django.contrib.auth.models import User

def users_context(request):
    users = User.objects.all()
    return {'users': users, 'user_groups': request.user.groups.values_list('name', flat=True)}

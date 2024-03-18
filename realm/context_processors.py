from .views import get_profile_picture_url

def profile_picture_context(request):
    return {'profile_picture_url': get_profile_picture_url(request)}

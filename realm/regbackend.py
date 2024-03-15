from registration.backends.simple.views import RegistrationView
from realm.forms import UserForm
from realm.models import UserProfile

class RealmRegistrationView(RegistrationView):
    form_class = UserForm
    success_url = 'realm:FavouriteCategories'
    def register(self, form_class):
        new_user = super(RealmRegistrationView, self).register(form_class)
        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.profilepicture = form_class.cleaned_data['profilepicture']
        user_profile.save()
        return new_user
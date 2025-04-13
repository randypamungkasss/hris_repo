from django.views.generic import ListView
from apps.profiles.models import Profile

class EmployeeListView(ListView):
    model = Profile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'
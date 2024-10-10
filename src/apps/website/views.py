from django.views.generic import TemplateView

from src.apps.accounts.models import CustomUser


class WebsiteView(TemplateView):
    template_name = "website/index.html"
    def get_context_data(self, **kwargs):
        print("GET TEAM..")
        team = CustomUser.objects.all()
        print("TEAM GET ,,",team)
        return {'team':team}


from django.contrib.sitemaps import Sitemap
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from src.apps.accounts.models import CustomUser
from src.apps.website.models import Blogs


class WebsiteView(TemplateView):
    template_name = "website/index.html"
    def get_context_data(self, **kwargs):
        print("GET TEAM..")
        team = CustomUser.objects.all()
        blogs = Blogs.objects.all()

        print("TEAM GET ,,",team)
        return {'team':team,'blogs':blogs}

class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(Blogs, id=blog_id)


class MoreBlogsView(ListView):
    model = Blogs
    template_name = 'blog/moreblogs.html'
    context_object_name = 'blogs'
    paginate_by = 10



class SiteMap(Sitemap):
    changefreq = "weekly"

    priority = 0.5

    def items(self):
        return Blogs.objects.all()  # Customize this to your needs

    def location(self, item):
        return f'/{item.id}/'  # Customize this URL path




# CONTACT US VIEW

# views.py

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings

# views.py

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import json


def contact_us_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')

            # Create the email content
            full_message = f"Message from {first_name} {last_name} ({email}):\n\n{message}"

            # Send email
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['escalators.tech@gmail.com'],  # Replace with the recipient email
                fail_silently=False,
            )

            # Return a success response
            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

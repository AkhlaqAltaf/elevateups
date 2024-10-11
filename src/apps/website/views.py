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
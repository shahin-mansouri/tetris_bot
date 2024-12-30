from django.views.generic import ListView
from .models import AwardBlog

class AwardBlogListView(ListView):
    model = AwardBlog
    template_name = "awards/list-blog.html"
    context_object_name = 'blogs'   

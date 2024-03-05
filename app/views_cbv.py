from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from app.forms import BlogForm
from app.models import Blog


# class CreateBlogView(View):
#     def get(self, request):
#         form = BlogForm()
#         context = {'form': form}
#         return render(request, 'create_blog.html', context)
#
#     def post(self, request):
#         form = BlogForm(request.POST, request.FILES)
#         if not request.user.is_authenticated:
#             messages.warning(request, 'Avval login qiling')
#             return redirect(reverse('app:create'))
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#         return redirect(reverse('app:home'))

class HomePageView(ListView):
    # model = Blog
    queryset = Blog.objects.published()
    template_name = 'home.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['text'] = "Bu blog project"
        return cd

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.is_published()
    #     return qs

class CreateBlogView(CreateView):
    template_name = 'create_blog.html'
    form_class = BlogForm
    success_url = '/'
    

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user
        blog.save()
        return super().form_valid(form)
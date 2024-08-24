from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import BlogPostForm
from catalog.models import BlogPost
from django.urls import reverse_lazy


class BlogPostListView(ListView):
    """
    Представление для отображения списка блогов.
    """
    model = BlogPost
    template_name = 'catalog/blogpost_list.html'
    context_object_name = 'posts'


    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    """
    Представление для отображения деталей блога.
    """
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    context_object_name = 'post'


    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    """
    Представление для создания нового блога.
    """
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'
    success_url = reverse_lazy('blogpost_list')


    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    """
    Представление для обновления существующего блога.
    """
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'


    def get_success_url(self):
        return reverse('blogpost_detail', args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    """
    Представление для удаления блога.
    """
    model = BlogPost
    template_name = 'catalog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

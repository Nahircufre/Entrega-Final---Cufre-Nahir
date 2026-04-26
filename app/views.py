from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Page
from .forms import PageForm


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')


class PageListView(ListView):
    model = Page
    template_name = 'app/pages.html'
    context_object_name = 'pages'


class PageDetailView(DetailView):
    model = Page
    template_name = 'app/page_detail.html'


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'app/page_form.html'
    success_url = reverse_lazy('pages')


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'app/page_form.html'
    success_url = reverse_lazy('pages')


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'app/page_delete.html'
    success_url = reverse_lazy('pages')
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Page, Mensaje
from .forms import PageForm


# 🏠 HOME
def index(request):
    return render(request, 'app/index.html')


# ℹ️ ABOUT
def about(request):
    return render(request, 'app/about.html')


# 📄 PAGES
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


# 💬 MENSAJERÍA
class InboxView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'app/inbox.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(
            destinatario=self.request.user
        ).order_by('-fecha')


class SentView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'app/sent.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(
            remitente=self.request.user
        ).order_by('-fecha')


class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    fields = ['destinatario', 'contenido']
    template_name = 'app/mensaje_form.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        messages.success(self.request, "Mensaje enviado correctamente ✅")
        return super().form_valid(form)


class MensajeDetailView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = 'app/mensaje_detail.html'
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Shop, ForumPost, JobPost, PromotionPost

def home(request):
    context = {
        'shop': Shop.objects.all()[:2],
        'forum': ForumPost.objects.all()[:1],
        'promo': PromotionPost.objects.all()[:1],
        'vacancy':JobPost.objects.all()[:1]
    }
    return render(request, 'web/home.html', context)

def forum(request):
    context = {
        'title':'Forum',
        'forum': ForumPost.objects.all()
    }
    return render(request, 'web/forum.html', context)

class ForumDetailView(DetailView):
    model = ForumPost

class ForumCreateView(CreateView):
    model = ForumPost
    fields = ['title', 'profile_picture', 'author', 'content']

    def form_valid(self, form):
        return super().form_valid(form)

def deals(request):
    context = {
        'title':'Deals',
        'promo': PromotionPost.objects.all()
    }
    return render(request, 'web/deals.html', context)

class PromoCreateView(CreateView):
    model = PromotionPost
    fields = ['title', 'logo', 'content', 'external_link', 'date_due']

    def form_valid(self, form):
        return super().form_valid(form)

def vacancy(request):
    context = {
        'title':'Vacancies',
        'vacancy':JobPost.objects.all()
    }
    return render(request, 'web/vacancy.html', context)

class JobCreateView(CreateView):
    model = JobPost
    fields = ['position', 'shop', 'logo', 'content', 'external_link', 'date_due']

class DealsDetailView(DetailView):
    model = PromotionPost

class VacancyDetailView(DetailView):
    model = JobPost

def shops(request):
    context = {
        'title': 'Store',
        'shops': Shop.objects.all()
    }
    return render(request, 'web/shops.html', context)

class ShopeCreateView(CreateView):
    model = Shop
    fields = ['name', 'logo', 'owner', 'location']
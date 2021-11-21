from django.urls import path
from . import views
from .views import ForumDetailView, VacancyDetailView, DealsDetailView, ForumCreateView, JobCreateView, PromoCreateView, ShopeCreateView

urlpatterns = [
    path('', views.home, name='web-home'),
    path('forum/', views.forum, name='web-forum'),
    path('forum/<int:pk>/', ForumDetailView.as_view(), name='forum-detail'),
    path('forum/create/', ForumCreateView.as_view(), name='forum-create'),
    path('deals/', views.deals, name='web-deals'),
    path('deals/<int:pk>/', DealsDetailView.as_view(), name='deals-detail'),
    path('deals/create/', PromoCreateView.as_view(), name='deals-create'),
    path('vacancies/', views.vacancy, name='web-vacancies'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='job-detail'),
    path('vacancies/create/', JobCreateView.as_view(), name='job-create'),
    path('store/', views.shops, name='web-store'),
    path('store/create', ShopeCreateView.as_view(), name='store-create'),
]
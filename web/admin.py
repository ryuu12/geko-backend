from django.contrib import admin
from .models import Shop, ForumPost, JobPost, PromotionPost

admin.site.register(Shop)
admin.site.register(ForumPost)
admin.site.register(JobPost)
admin.site.register(PromotionPost)
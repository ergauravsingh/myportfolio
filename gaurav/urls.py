
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('project/<int:project_id>', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),   #2
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),  #5
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),  #5
]
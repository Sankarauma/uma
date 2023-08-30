from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_blog, name='add_blog'),
    path('list/', views.list_blogs, name='list_blogs'),
    path('view/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),  # Add this line
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),
]



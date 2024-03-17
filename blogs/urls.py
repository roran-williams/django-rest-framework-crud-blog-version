from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateBlogAPIView.as_view(), name='get_post_blogs'),
    path('<int:pk>/', views.RetrieveUpdateDestroyBlogAPIView.as_view(), name='get_delete_update_blog'),
    path('<str:topic>/', views.ListCreateBlogAPIView.as_view(), name='topic_blog'),  # Endpoint for retrieving blogs by topic
]

from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
]

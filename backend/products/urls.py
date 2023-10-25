from django.urls import path
from . import views


urlpatterns = [
    path('', views.proudct_list_create_view),
    path('<int:pk>/',views.product_detail_view),
    path('<int:pk>/update/',views.ProductUpdateView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view()),
]

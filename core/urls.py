from django.urls import path

from .views import index, produtos, add_produtos, edit_produtos, excluir_produtos

urlpatterns = [
    path('', index, name='dashboard-index'),
    path('produtos', produtos, name='produtos'),
    path('add_produtos', add_produtos, name='add_produtos'),
    path('edit_produtos/<str:pk>', edit_produtos, name='edit_produtos'),
    path('excluir_produtos/<str:pk>', excluir_produtos, name='excluir_produtos'),
]
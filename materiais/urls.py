from django.urls import path
from .views import materials_list, new_material, update_material, delete_material

urlpatterns = [
	path('lista/', materials_list, name='materials_list'),
	path('novo/', new_material, name='new_material'),
	path('atualizar/<int:id>/', update_material, name='update_material'),
	path('excluir/<int:id>/', delete_material, name='delete_material'),
]
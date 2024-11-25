from django.urls import path
from .views import project_list
from .views import get_projects


urlpatterns = [
    path('<int:item_id>', project_list, name='project_list'),
    path('', project_list, name='get_all_items'),
    path('items/', get_projects, name='get_all_items'),
    path('items/<int:item_id>/', get_projects, name='get_item_by_id'),
]
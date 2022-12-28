from django.urls import path
from .views import index
from .views import by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
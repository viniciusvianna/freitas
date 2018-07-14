from django.urls import path
from .views import student_page

urlpatterns = [
	path('<str:name>/', student_page),
]

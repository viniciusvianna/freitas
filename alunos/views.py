from django.shortcuts import render
from .models import Aluno

def student_page(request, name):
	# student = Aluno.object.get(firstName='Joao')
	return render(request, 'student.html', {'sName': name})

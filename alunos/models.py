from django.db import models

class Aluno(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	email = models.EmailField(max_length=254)
	birthDay = models.DateField()
	picture = models.ImageField(upload_to='alunos_fotos', null=True, blank=True)

	def __str__(self):
		return self.firstName + ' ' + self.lastName


from django.db import models

class Material(models.Model):
	QUIMICA = 'QUI'
	FISICA = 'FIS'
	BIOLOGIA = 'BIO'
	MATEMATICA = 'MAT'
	PORTUGUES = 'POR'
	REDACAO = 'RED'
	HISTORIA = 'HIS'
	GEOGRAFIA = 'GEO'

	SUBJECT_CHOICES = (
		(QUIMICA, 'Química'),
		(FISICA, 'Física'),
		(BIOLOGIA, 'Biologia'),
		(MATEMATICA, 'Matemática'),
		(PORTUGUES, 'Português'),
		(REDACAO, 'Redação'),
		(HISTORIA, 'História'),
		(GEOGRAFIA, 'Geografia'),
	)


	title = models.CharField(max_length=60)
	slug = models.SlugField(max_length=30, null=True, blank=True)
	subject = models.CharField(max_length=3, choices=SUBJECT_CHOICES, default=QUIMICA)
	file = models.FileField(upload_to='materiais/', null=True, blank=True)

	def __str__(self):
		return self.title

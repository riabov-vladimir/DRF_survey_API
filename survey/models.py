from django.db import models


class Poll(models.Model):

	name = models.CharField(max_length=255, verbose_name='Название', unique=True)
	date_started = models.DateField(auto_now_add=True, verbose_name='Дата начала опроса')
	date_ended = models.DateField(null=True, verbose_name='Дата начала опроса')
	description = models.TextField(null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('date_started',)
		verbose_name = 'опрос'
		verbose_name_plural = 'опросы'

